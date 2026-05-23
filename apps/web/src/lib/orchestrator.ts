import { AGENT_REGISTRY } from './agent-registry';
import { Agent, Task, OrchestrationEvent, ExecutionContext } from '../types/agent';

export interface RoutingResult {
  selectedAgent: Agent | null;
  events: OrchestrationEvent[];
  reason: string;
}

export class Orchestrator {
  private events: OrchestrationEvent[] = [];

  classifyIntent(task: Task): string {
    const keywords = task.description.toLowerCase();
    if (keywords.includes('research') || keywords.includes('analyze')) return 'research';
    if (keywords.includes('bug') || keywords.includes('debug')) return 'debug';
    if (keywords.includes('security') || keywords.includes('vuln')) return 'security';
    if (keywords.includes('refactor') || keywords.includes('optimize')) return 'refactor';
    if (keywords.includes('doc') || keywords.includes('document')) return 'documentation';
    if (keywords.includes('test')) return 'test';
    if (keywords.includes('deploy')) return 'deployment';
    return 'orchestrator';
  }

  matchAgent(intent: string, capabilities: string[]): Agent | null {
    return AGENT_REGISTRY.find(agent => 
      agent.role === intent || 
      agent.capabilities.some(cap => capabilities.includes(cap))
    ) || null;
  }

  routeTask(task: Task, context: ExecutionContext): RoutingResult {
    const intent = this.classifyIntent(task);
    const selectedAgent = this.matchAgent(intent, task.description.toLowerCase().split(' '));

    const event: OrchestrationEvent = {
      id: `evt_${Date.now()}`,
      timestamp: new Date().toISOString(),
      type: selectedAgent ? 'agent_selected' : 'error',
      taskId: task.id,
      agentId: selectedAgent?.id,
      details: selectedAgent ? `Routed to ${selectedAgent.name}` : 'No matching agent found'
    };

    this.events.push(event);

    return {
      selectedAgent,
      events: this.events,
      reason: selectedAgent ? 'Capability match' : 'No agent matches intent'
    };
  }

  getNoAgentFallback(task: Task): RoutingResult {
    return {
      selectedAgent: AGENT_REGISTRY[0], // Orchestrator fallback
      events: [],
      reason: 'Fallback to Orchestrator'
    };
  }
}

export const orchestrator = new Orchestrator();
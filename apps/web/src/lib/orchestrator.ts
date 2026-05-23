import { AGENT_REGISTRY } from './agent-registry';
import { Agent, Task } from '../types/agent';

export interface RoutingResult {
  selectedAgent: Agent | null;
  events: any[];
  reason: string;
}

export class Orchestrator {
  private events: any[] = [];

  classifyIntent(task: Task): string {
    const keywords = task.description.toLowerCase();
    if (keywords.includes('research') || keywords.includes('analyze')) return 'research';
    if (keywords.includes('bug') || keywords.includes('debug')) return 'debug';
    if (keywords.includes('security')) return 'security';
    if (keywords.includes('refactor')) return 'refactor';
    if (keywords.includes('doc')) return 'documentation';
    if (keywords.includes('test')) return 'test';
    if (keywords.includes('deploy')) return 'deployment';
    return 'orchestrator';
  }

  matchAgent(intent: string): Agent | null {
    return AGENT_REGISTRY.find(a => a.name.toLowerCase().includes(intent)) || AGENT_REGISTRY[0];
  }

  routeTask(task: Task): RoutingResult {
    const intent = this.classifyIntent(task);
    const selectedAgent = this.matchAgent(intent);

    const event = {
      id: `evt_${Date.now()}`,
      timestamp: new Date().toISOString(),
      type: 'agent_selected',
      taskId: task.id,
      agentId: selectedAgent.id,
      details: `Routed to ${selectedAgent.name}`
    };

    this.events.push(event);

    return {
      selectedAgent,
      events: this.events,
      reason: 'Capability match'
    };
  }
}

export const orchestrator = new Orchestrator();
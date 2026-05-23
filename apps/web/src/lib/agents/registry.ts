import { Agent } from '../types/agent';

export const agentRegistry: Agent[] = [
  { id: 'orchestrator', name: 'Orchestrator', capabilities: ['task-routing', 'coordination'], status: 'idle' }
];
export interface Agent {
  id: string;
  name: string;
  capabilities: string[];
  status: 'idle' | 'active' | 'error';
}

export interface Task {
  id: string;
  agentId: string;
  description: string;
  status: string;
}

export interface Workflow {
  id: string;
  tasks: Task[];
}
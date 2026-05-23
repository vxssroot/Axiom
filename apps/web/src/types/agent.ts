export type AgentRole = 'orchestrator' | 'research' | 'debug' | 'security' | 'refactor' | 'documentation' | 'test' | 'deployment';

export type AgentStatus = 'idle' | 'active' | 'busy' | 'error' | 'offline';

export type AgentCapability = 'code_analysis' | 'research' | 'debugging' | 'security_scan' | 'refactoring' | 'doc_generation' | 'testing' | 'deployment';

export interface Agent {
  id: string;
  name: string;
  role: AgentRole;
  description: string;
  capabilities: AgentCapability[];
  permissions: string[];
  status: AgentStatus;
  modelPreference: string;
  memoryScope: 'global' | 'project' | 'session';
  createdAt: string;
  updatedAt: string;
}

export type TaskPriority = 'low' | 'medium' | 'high' | 'critical';

export type TaskStatus = 'pending' | 'in_progress' | 'completed' | 'failed' | 'blocked';

export interface Task {
  id: string;
  title: string;
  description: string;
  priority: TaskPriority;
  status: TaskStatus;
  assignedAgentId?: string;
  dependencies?: string[];
  createdAt: string;
  updatedAt: string;
}

export interface Workflow {
  id: string;
  name: string;
  tasks: Task[];
  assignedAgents: string[];
  status: 'draft' | 'running' | 'completed' | 'failed';
  dependencies: Record<string, string[]>;
  eventHistory: OrchestrationEvent[];
  createdAt: string;
  updatedAt: string;
}

export interface OrchestrationEvent {
  id: string;
  timestamp: string;
  type: 'task_routed' | 'agent_selected' | 'execution_started' | 'error';
  taskId?: string;
  agentId?: string;
  details: string;
}

export interface ExecutionContext {
  projectId?: string;
  userId: string;
  sessionId: string;
  memoryReferences: MemoryReference[];
}

export interface MemoryReference {
  id: string;
  type: 'code' | 'doc' | 'task';
  reference: string;
}

export interface ToolPermission {
  tool: string;
  level: 'read' | 'write' | 'execute';
}

export interface AgentCardProps {
  agent: Agent;
  activeTasks?: number;
}
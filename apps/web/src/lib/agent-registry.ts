import { Agent, AgentRole, AgentStatus, AgentCapability } from '../types/agent';

export const AGENT_REGISTRY: Agent[] = [
  {
    id: 'orchestrator-001',
    name: 'Orchestrator',
    role: 'orchestrator',
    description: 'Routes tasks, manages workflows, and coordinates agents.',
    capabilities: ['code_analysis', 'research'],
    permissions: ['route_tasks', 'manage_workflows'],
    status: 'idle',
    modelPreference: 'gpt-4o',
    memoryScope: 'global',
    createdAt: '2026-05-01T00:00:00Z',
    updatedAt: '2026-05-23T12:00:00Z'
  },
  {
    id: 'research-001',
    name: 'Research',
    role: 'research',
    description: 'Performs deep code and requirement research.',
    capabilities: ['research'],
    permissions: ['read_code', 'query_vector'],
    status: 'idle',
    modelPreference: 'claude-3',
    memoryScope: 'project',
    createdAt: '2026-05-01T00:00:00Z',
    updatedAt: '2026-05-23T12:00:00Z'
  },
  {
    id: 'debug-001',
    name: 'Debugger',
    role: 'debug',
    description: 'Identifies and resolves bugs in codebase.',
    capabilities: ['debugging'],
    permissions: ['read_code', 'execute_tests'],
    status: 'idle',
    modelPreference: 'gpt-4o',
    memoryScope: 'project',
    createdAt: '2026-05-01T00:00:00Z',
    updatedAt: '2026-05-23T12:00:00Z'
  },
  {
    id: 'security-001',
    name: 'Security',
    role: 'security',
    description: 'Performs security audits and vulnerability scans.',
    capabilities: ['security_scan'],
    permissions: ['read_code', 'scan_vulns'],
    status: 'idle',
    modelPreference: 'gpt-4o',
    memoryScope: 'project',
    createdAt: '2026-05-01T00:00:00Z',
    updatedAt: '2026-05-23T12:00:00Z'
  },
  {
    id: 'refactor-001',
    name: 'Refactor',
    role: 'refactor',
    description: 'Optimizes and refactors code structures.',
    capabilities: ['refactoring'],
    permissions: ['write_code'],
    status: 'idle',
    modelPreference: 'claude-3',
    memoryScope: 'project',
    createdAt: '2026-05-01T00:00:00Z',
    updatedAt: '2026-05-23T12:00:00Z'
  },
  {
    id: 'doc-001',
    name: 'Documentation',
    role: 'documentation',
    description: 'Generates and maintains documentation.',
    capabilities: ['doc_generation'],
    permissions: ['write_docs'],
    status: 'idle',
    modelPreference: 'gpt-4o',
    memoryScope: 'project',
    createdAt: '2026-05-01T00:00:00Z',
    updatedAt: '2026-05-23T12:00:00Z'
  },
  {
    id: 'test-001',
    name: 'Tester',
    role: 'test',
    description: 'Creates and runs tests.',
    capabilities: ['testing'],
    permissions: ['execute_tests', 'write_tests'],
    status: 'idle',
    modelPreference: 'gpt-4o',
    memoryScope: 'project',
    createdAt: '2026-05-01T00:00:00Z',
    updatedAt: '2026-05-23T12:00:00Z'
  },
  {
    id: 'deploy-001',
    name: 'Deployment',
    role: 'deployment',
    description: 'Handles deployment pipelines and releases.',
    capabilities: ['deployment'],
    permissions: ['deploy', 'ci_cd'],
    status: 'idle',
    modelPreference: 'gpt-4o',
    memoryScope: 'global',
    createdAt: '2026-05-01T00:00:00Z',
    updatedAt: '2026-05-23T12:00:00Z'
  }
];
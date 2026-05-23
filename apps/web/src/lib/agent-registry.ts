import { Agent } from '../types/agent';

export const AGENT_REGISTRY: Agent[] = [
  {
    id: 'orchestrator-001',
    name: 'Orchestrator',
    capabilities: ['routing', 'coordination'],
    status: 'idle'
  },
  {
    id: 'research-001',
    name: 'Research',
    capabilities: ['research'],
    status: 'idle'
  },
  {
    id: 'debug-001',
    name: 'Debugger',
    capabilities: ['debugging'],
    status: 'idle'
  },
  {
    id: 'security-001',
    name: 'Security',
    capabilities: ['security_scan'],
    status: 'idle'
  },
  {
    id: 'refactor-001',
    name: 'Refactor',
    capabilities: ['refactoring'],
    status: 'idle'
  },
  {
    id: 'doc-001',
    name: 'Documentation',
    capabilities: ['doc_generation'],
    status: 'idle'
  },
  {
    id: 'test-001',
    name: 'Tester',
    capabilities: ['testing'],
    status: 'idle'
  },
  {
    id: 'deploy-001',
    name: 'Deployment',
    capabilities: ['deployment'],
    status: 'idle'
  }
];
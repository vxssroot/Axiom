'use client';
import { Agent } from '../types/agent';

interface AgentCardProps {
  agent: any;
  activeTasks?: number;
}

export function AgentCard({ agent, activeTasks = 0 }: AgentCardProps) {
  const statusColor = 'bg-green-500/20 text-green-400';

  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6 hover:border-zinc-700 transition-all group">
      <div className="flex items-start justify-between">
        <div>
          <div className="font-semibold text-xl tracking-tight">{agent.name}</div>
          <div className="text-sm text-zinc-500 mt-1">Specialized Agent</div>
        </div>
        <div className={`px-3 py-1 text-xs rounded-full font-mono ${statusColor}`}>
          {agent.status}
        </div>
      </div>

      <div className="mt-6 text-sm text-zinc-400">
        Core capabilities for engineering tasks.
      </div>

      <div className="mt-8 grid grid-cols-2 gap-4 text-xs">
        <div>
          <div className="text-zinc-500">Capabilities</div>
          <div className="font-mono text-zinc-400">{agent.capabilities.length}</div>
        </div>
        <div>
          <div className="text-zinc-500">Active</div>
          <div className="font-mono text-zinc-400">{activeTasks}</div>
        </div>
      </div>
    </div>
  );
}
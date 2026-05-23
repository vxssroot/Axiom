'use client';
import { Agent } from '../types/agent';

interface AgentCardProps {
  agent: Agent;
  activeTasks?: number;
}

export function AgentCard({ agent, activeTasks = 0 }: AgentCardProps) {
  const statusColor = {
    idle: 'bg-green-500/20 text-green-400',
    active: 'bg-blue-500/20 text-blue-400',
    busy: 'bg-yellow-500/20 text-yellow-400',
    error: 'bg-red-500/20 text-red-400',
    offline: 'bg-gray-500/20 text-gray-400',
  }[agent.status];

  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6 hover:border-zinc-700 transition-all group">
      <div className="flex items-start justify-between">
        <div>
          <div className="font-semibold text-xl tracking-tight">{agent.name}</div>
          <div className="text-sm text-zinc-500 mt-1 capitalize">{agent.role}</div>
        </div>
        <div className={`px-3 py-1 text-xs rounded-full font-mono ${statusColor}`}>
          {agent.status}
        </div>
      </div>

      <div className="mt-6 text-sm text-zinc-400 line-clamp-2">
        {agent.description}
      </div>

      <div className="mt-6 flex flex-wrap gap-1">
        {agent.capabilities.slice(0, 3).map((cap, i) => (
          <div key={i} className="text-[10px] px-2 py-0.5 bg-zinc-800 rounded text-zinc-500">
            {cap.replace('_', ' ')}
          </div>
        ))}
      </div>

      <div className="mt-8 grid grid-cols-2 gap-4 text-xs">
        <div>
          <div className="text-zinc-500">Permissions</div>
          <div className="font-mono text-zinc-400">{agent.permissions.length}</div>
        </div>
        <div>
          <div className="text-zinc-500">Memory</div>
          <div className="font-mono text-zinc-400 capitalize">{agent.memoryScope}</div>
        </div>
      </div>

      <div className="mt-4 text-xs text-zinc-500">
        Active tasks: {activeTasks}
      </div>
    </div>
  );
}
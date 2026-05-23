'use client';
import { useState, useEffect } from 'react';
import { AGENT_REGISTRY } from '../lib/agent-registry';
import { AgentCard } from '../components/agent-card';
import { orchestrator } from '../lib/orchestrator';
import { Task, Workflow } from '../types/agent';

export default function AxiomDashboard() {
  const [agents] = useState(AGENT_REGISTRY);
  const [workflows, setWorkflows] = useState<Workflow[]>([]);
  const [timeline, setTimeline] = useState<any[]>([]);
  const [systemStatus, setSystemStatus] = useState('operational');

  // Demo workflow
  useEffect(() => {
    const demoTask: Task = {
      id: 'task-1',
      title: 'Analyze codebase structure',
      description: 'Research architecture and identify key modules',
      priority: 'high',
      status: 'pending',
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    };

    const result = orchestrator.routeTask(demoTask, { userId: 'demo', sessionId: 'demo' });
    setTimeline(result.events);
  }, []);

  return (
    <div className="min-h-screen bg-[#0a0a0a] text-white p-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="flex justify-between items-end mb-12">
          <div>
            <div className="text-5xl font-semibold tracking-[-3px]">AXIOM</div>
            <div className="text-xl text-zinc-500 mt-1">Engineering Operating System</div>
          </div>
          <div className="flex items-center gap-3">
            <div className="px-4 py-2 bg-zinc-900 border border-zinc-800 rounded-xl text-sm">Phase 1.5 Foundation</div>
            <div className={`px-4 py-2 rounded-xl text-sm ${systemStatus === 'operational' ? 'bg-emerald-500/10 text-emerald-400' : 'bg-red-500/10 text-red-400'}`}>System {systemStatus}</div>
          </div>
        </div>

        {/* Overview Cards */}
        <div className="grid grid-cols-4 gap-6 mb-12">
          <div className="bg-zinc-900 border border-zinc-800 rounded-3xl p-8">
            <div className="text-4xl font-semibold">8</div>
            <div className="text-sm text-zinc-500 mt-2">Active Agents</div>
          </div>
          <div className="bg-zinc-900 border border-zinc-800 rounded-3xl p-8">
            <div className="text-4xl font-semibold">3</div>
            <div className="text-sm text-zinc-500 mt-2">Running Workflows</div>
          </div>
          <div className="bg-zinc-900 border border-zinc-800 rounded-3xl p-8">
            <div className="text-4xl font-semibold tracking-tight">12</div>
            <div className="text-sm text-zinc-500 mt-2">Tasks Routed</div>
          </div>
          <div className="bg-zinc-900 border border-zinc-800 rounded-3xl p-8">
            <div className="text-4xl font-semibold">99.8%</div>
            <div className="text-sm text-zinc-500 mt-2">Uptime</div>
          </div>
        </div>

        {/* Agent Grid */}
        <div className="mb-12">
          <div className="flex justify-between items-center mb-6">
            <div className="text-2xl font-semibold tracking-tight">Agent Fleet</div>
            <div className="text-sm text-zinc-500">Specialized for autonomous engineering</div>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {agents.map(agent => (
              <AgentCard key={agent.id} agent={agent} activeTasks={Math.floor(Math.random() * 3)} />
            ))}
          </div>
        </div>

        {/* Orchestration Timeline */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="lg:col-span-2 bg-zinc-900 border border-zinc-800 rounded-3xl p-8">
            <div className="text-xl font-semibold mb-6">Orchestration Timeline</div>
            <div className="space-y-4">
              {timeline.length > 0 ? timeline.map((event, i) => (
                <div key={i} className="flex gap-4 text-sm border-l border-zinc-800 pl-6">
                  <div className="text-zinc-500 w-32 shrink-0">{new Date(event.timestamp).toLocaleTimeString()}</div>
                  <div>{event.details}</div>
                </div>
              )) : <div className="text-zinc-500">No events yet</div>}
            </div>
          </div>

          {/* Workflow Preview */}
          <div className="bg-zinc-900 border border-zinc-800 rounded-3xl p-8">
            <div className="text-xl font-semibold mb-6">Active Workflows</div>
            {workflows.length === 0 && (
              <div className="text-zinc-500 italic">No workflows running. Create one to begin orchestration.</div>
            )}
          </div>
        </div>

        {/* System Status */}
        <div className="mt-12 border border-zinc-800 bg-zinc-950 rounded-3xl p-8 text-sm">
          <div className="uppercase tracking-[2px] text-zinc-500 mb-4">SYSTEM STATUS</div>
          <div className="grid grid-cols-2 gap-x-12">
            <div>Orchestrator: Online</div>
            <div>Memory Layer: Ready</div>
            <div>Agent Registry: 8 loaded</div>
            <div>Routing Engine: v1.5</div>
          </div>
        </div>
      </div>
    </div>
  );
}
'use client';
import { useEffect, useState } from 'react';
import { api } from '../../lib/api';
export default function RepoPage({ params }: { params: { id: string } }) {
  const [summary, setSummary] = useState('');
  const [loading, setLoading] = useState(true);
  useEffect(() => { api.post('/repos/summarize', { repo_id: params.id }).then(r => setSummary(r.content)).catch(() => setSummary('No summary available. Index the repo first.')).finally(() => setLoading(false)); }, [params.id]);
  const runAction = async (endpoint: string) => { try { const r = await api.post(endpoint, { repo_id: params.id }); alert(r.content); } catch (e: any) { alert(e.message); } };
  return <div className='flex h-screen bg-[#0a0a0a] text-white'><div className='w-72 border-r border-gray-800 p-8'><div className='font-semibold text-2xl'>Axiom</div></div><div className='flex-1 p-10'><div className='max-w-5xl'><div className='text-4xl font-semibold tracking-tight'>{params.id}</div><div className='mt-8 card p-6 rounded-3xl'><div className='text-sm text-gray-400 mb-4'>AI Summary</div>{loading ? 'Loading...' : <div className='text-sm leading-relaxed text-gray-300'>{summary}</div>}</div><div className='mt-6 grid grid-cols-2 gap-4'><div className='card p-6 rounded-3xl cursor-pointer' onClick={() => runAction('/repos/review')}>Run Review</div><div className='card p-6 rounded-3xl cursor-pointer' onClick={() => runAction('/repos/architecture')}>Architecture Overview</div></div></div></div></div>;
}
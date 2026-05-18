'use client';
import { useEffect, useState } from 'react';
import { api } from '../lib/api';
export default function Repos() {
  const [repos, setRepos] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  useEffect(() => { api.get('/github/repos').then(r => setRepos(r.repos || [])).catch(e => setError(e.message)).finally(() => setLoading(false)); }, []);
  const handleImport = async () => {
    const url = prompt('Enter GitHub repo URL (e.g. https://github.com/user/repo)');
    if (!url) return;
    try { await api.post('/github/import', { repo_url: url }); alert('Import started - check dashboard'); } catch (e: any) { alert(e.message); }
  };
  if (loading) return <div className='p-10 text-white'>Loading repos...</div>;
  if (error) return <div className='p-10 text-red-400'>Error: {error}</div>;
  return <div className='flex h-screen bg-[#0a0a0a] text-white'><div className='w-72 border-r border-gray-800 p-8'><div className='font-semibold text-2xl'>Axiom</div></div><div className='flex-1 p-10'><div className='max-w-5xl'><div className='flex justify-between items-center'><div className='text-4xl font-semibold tracking-tight'>Repositories</div><button onClick={handleImport} className='px-6 py-2.5 bg-white text-black rounded-2xl text-sm'>Import from GitHub</button></div><div className='mt-8 space-y-3'>{repos.length === 0 ? <div className='text-gray-400'>No repositories found. Import one to get started.</div> : repos.map((r, i) => <div key={i} className='card p-5 rounded-2xl flex justify-between items-center'><div><div className='font-medium'>{r}</div><div className='text-xs text-gray-500'>Indexed</div></div><div className='text-xs px-3 py-1 bg-emerald-900 text-emerald-400 rounded'>Ready</div></div>)}</div></div></div></div>;
}
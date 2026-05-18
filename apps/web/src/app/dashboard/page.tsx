'use client';
import { useEffect, useState } from 'react';
import { api } from '../lib/api';
export default function Dashboard() {
  const [user, setUser] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => { api.get('/auth/me').then(setUser).catch(() => setUser(null)).finally(() => setLoading(false)); }, []);
  if (loading) return <div className='min-h-screen flex items-center justify-center bg-[#0a0a0a] text-white'>Loading...</div>;
  return <div className='flex h-screen bg-[#0a0a0a] text-white'><div className='w-72 border-r border-gray-800 p-8'><div className='font-semibold text-2xl tracking-tight'>Axiom</div><div className='mt-12 text-sm uppercase tracking-[1px] text-gray-500'>Workspace</div><div className='mt-4 text-lg'>Dashboard</div><div className='mt-3 text-lg text-gray-400'>Repositories</div><div className='mt-3 text-lg text-gray-400'>Intelligence</div><div className='mt-3 text-lg text-gray-400'>Settings</div></div><div className='flex-1 p-10'><div className='max-w-5xl'><div className='flex items-end justify-between'><div><div className='text-6xl font-semibold tracking-[-2px]'>Good evening{user ? `, ${user.github_login}` : ''}.</div><div className='text-2xl text-gray-400 mt-1'>{user ? '3 repositories indexed' : 'Sign in to get started'}</div></div>{user && <a href='/repos' className='px-6 py-2.5 bg-white text-black rounded-2xl text-sm font-medium'>Import repo</a>}</div>{!user && <div className='mt-10 text-gray-400'>Please <a href='/login' className='underline'>sign in</a> to access your repositories and AI tools.</div>}</div></div></div>;
}
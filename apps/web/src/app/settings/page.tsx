'use client';
import { useEffect, useState } from 'react';
import { api } from '../lib/api';
export default function Settings() {
  const [user, setUser] = useState<any>(null);
  useEffect(() => { api.get('/auth/me').then(setUser).catch(() => {}); }, []);
  return <div className='p-10 max-w-2xl text-white'><div className='text-4xl font-semibold tracking-tight'>Settings</div><div className='mt-8 card p-6 rounded-3xl'><div className='text-sm text-gray-400'>GitHub</div><div className='mt-2'>{user ? `Connected as ${user.github_login}` : 'Not connected - sign in from login page'}</div></div></div>;
}
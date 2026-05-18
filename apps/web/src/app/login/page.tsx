'use client';
import { useState } from 'react';
export default function Login() {
  const [loading, setLoading] = useState(false);
  const handleLogin = () => { setLoading(true); window.location.href = 'http://localhost:8000/auth/github/login'; };
  return <div className='min-h-screen flex items-center justify-center bg-[#0a0a0a]'><div className='max-w-md text-center'><h2 className='text-5xl font-semibold tracking-tight'>Sign in</h2><p className='mt-4 text-gray-400'>Connect GitHub for private repo access and intelligence.</p><button onClick={handleLogin} disabled={loading} className='mt-8 w-full py-4 bg-white text-black rounded-2xl font-medium disabled:opacity-50'>{loading ? 'Connecting...' : 'Continue with GitHub'}</button><p className='mt-6 text-xs text-gray-500'>Backend-controlled • Secure OAuth</p></div></div>;
}
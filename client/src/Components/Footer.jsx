import React from 'react'
import githubLogo from '../assets/Github.svg';
import linkedinLogo from '../assets/Linkedin.svg';


const Footer = () => {
  return (
    <div className='flex gap-5 align-middle justify-center text-center bg-slate-50 border-2 border-slate-200 rounded-t-md w-screen p-3'>
        <a href='https://github.com/sidharthd7'>
          <img className='h-5 w-5' src={githubLogo}/>
        </a>
        <a href='https://www.linkedin.com/in/sidharth-dhawan/'>
          <img className='h-5 w-5' src={linkedinLogo}/>
        </a>
    </div>
  )
}

export default Footer
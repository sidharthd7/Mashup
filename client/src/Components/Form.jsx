import React, {useState} from 'react'
import {Button, Input} from "@material-tailwind/react"

const Form = ({onSubmit}) => {
    const[formData, setFormData] = useState({
        singer: "",
        num_songs: "",
        clip_duration: "",
        email_id: ""
    });

    const handleChange = (e) =>{
        setFormData({...formData, [e.target.name]:e.target.value});
    };

    const handleSubmit = (e) =>{
        e.preventDefault();
        onSubmit(formData);
    }

  return (
    <form onSubmit={handleSubmit} className='flex flex-col justify-center gap-4 text-base'>

        <div className='fields flex flex-col gap-2'>
            <div className='singer-name gap-2 flex items-center'>
                <p className='w-36'>Singer: </p>
                <Input type='text' size='sm' name='singer' value={formData.singer} onChange={handleChange} placeholder='Who is your favourite?'/>
            </div>
            <div className='videos-no gap-2 flex items-center'>
                <p className='w-36'>No. of videos: </p>
                <Input type='number' size='sm' name='num_songs' value={formData.numVideos} onChange={handleChange} placeholder='10'/>
            </div>
            <div className='duration gap-2 flex items-center'>
                <p className='w-36'>Duration: </p>
                <Input type='number' size='sm' name='clip_duration' value={formData.duration} onChange={handleChange} placeholder='10 (in seconds)'/>
            </div>
            <div className='email gap-2 flex items-center'>
                <p className='w-36'>Email Id: </p>
                <Input type='email' size='sm' name='email_id' value={formData.email} onChange={handleChange} placeholder='abc@gmail.com'/>
            </div>
        </div>
        {/* <button type='submit' className='px-4 py-1 '>
            Submit
        </button> */}
        <Button type='submit' size='md' variant='gradient'>Submit</Button>
    </form>
  )
}

export default Form
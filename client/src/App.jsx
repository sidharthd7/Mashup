import React, { useState } from "react";
import Form from "./Components/Form";
import Result from "./Components/Result";

function App(){
  const [result, setResult] = useState("");

  const handleSubmit = async (formData) =>{
    const response = await fetch("http://localhost:5000/api/process",{
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(formData),
    })
    
    const data = await response.json();
    setResult(data.message);
  }

  return (
    <div className="App flex flex-col justify-center items-center w-auto h-screen">
      {/* <div className="flex flex-col justify-center align-middle"> */}
        <h1 className="py-3 font-bold text-center text-3xl">Mashup</h1>
        <Form onSubmit={handleSubmit}/>
        {result && <Result result={result}/>}
      {/* </div> */}
    </div>
  )
}

export default App;
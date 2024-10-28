import React, { useState } from "react";
import Form from "./Components/Form";
import Result from "./Components/Result";
import Footer from "./Components/Footer";

function App(){
  const [result, setResult] = useState("");

  const handleSubmit = async (formData) =>{
    try{
      const response = await fetch("http://localhost:5000/api/process",{
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(formData),
      })
      
      const data = await response.json();
      setResult(data.message);
    } catch (error){
      console.error('Error during submission', error);
      setResult('An error occured.');
    }
  }

  return (
    <div className="App flex flex-col min-h-screen bg-gray-50">

      <div className="flex flex-grow flex-col justify-center items-center">
        <h1 className="py-3 font-bold text-center text-3xl">Mashup</h1>
        <Form onSubmit={handleSubmit}/>
        {result && <Result result={result}/>}
      </div>

      <div className="mb-0 "><Footer/></div>
    </div>
  )
}

export default App;
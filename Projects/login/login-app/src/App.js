import React,{useState} from 'react';


function App() {
  const [data, setData]=useState({
    username: "",
    password: ""

  })
  const {username, password }=data;
  const changeHandler =e =>{
    setData({...data, [e.target.name]:[e.target.value]})
  }
  const submitHandler = e =>{
    e.preventDefault();
    console.log(data)

  }
  return (
    <div>
      <center>
        <form onSubmit={submitHandler}> 
        

          <input type='text' name='username' value={username} onChange={changeHandler}/> <br/>
          <input type='password' name='password' value={password} onChange={changeHandler}/><br/>
          <input type='submit' name='Login' /><br/>
        </form>


      </center>
     
      
    </div>
  );
}

export default App;

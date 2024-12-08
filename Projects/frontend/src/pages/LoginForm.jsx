import React from 'react'
import '/Users/sowmyajavvadi/Projects/frontend/src/Components/LoginForm/LoginForm.css';
import { FaUser, FaLock} from "react-icons/fa";

const LoginForm = () => {
  return (
    <div class='container'>
        <div class="wrapper">
        <form action=''>
            <h1>Login</h1>
            <div className='input-box'>
                <label>User Name</label><br/>
                <input type='text' placeholder='Enter your Username' required />
                <FaUser className='icon' />
            </div>
            <div className='input-box'>
            <label>Password</label><br/>
                <input type='password' placeholder='Enter your Password' required />
                <FaLock className='icon'/>
            </div>
            <div className='remember-forgot'>
                <label><input type='checkbox'/> Remember me </label>
            </div>
            <button type='submit'>Login</button>
        </form>
        
      
    </div>
    </div>
    
  )
}

export default LoginForm

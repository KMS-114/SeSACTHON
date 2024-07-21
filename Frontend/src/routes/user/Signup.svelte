<script>
    import { navigate } from 'svelte-routing';
    import { writable } from 'svelte/store';

    let userid = '';
    let usergroup;
    let username = '';
    let password = '';
    let affiliation = '';

    let error = null;
  
    async function signup(event) {
      event.preventDefault();
      const timestamp = new Date().toISOString();

      // integer로 변경
      const userGroupInt = parseInt(usergroup, 10);
      console.log(userGroupInt);
      try{
      const response = await fetch('http://localhost:8000/user/create/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: username,
          userGroup: usergroup,
          password: password,
          affiliation: affiliation,
          createdAt:  timestamp,
          updatedAt: timestamp
        }),

      });
  
      if (response.ok) {
        alert('Signup successful');
        navigate('/login', { replace: true });
      } else {
        console.log()
        alert('Signup failed');
      }
    }
    catch(err){
      error = err.message
      console.log(error);
    }
    }

    function handleIntegerInput(event, index, key) {
        const value = parseInt(event.target.value, 10);
        userData[index][key] = isNaN(value) ? '' : value;
    }
</script>
  
<style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
  
    body, html {
      height: 100%;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: #f8f9fa;
    }
  
    .page-wrapper {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      width: 100%;
    }
  
    .section_half-half {
      display: flex;
      width: 100%;
      height: 100%;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      background-color: white;
    }
  
    .half-width {
      width: 50%;
      padding: 40px;
      box-sizing: border-box;
    }
  
    .form-container {
      width: 100%;
    }
  
    .h1-small {
      font-size: 24px;
      font-weight: 600;
    }
  
    .input-wrapper {
      margin-bottom: 20px;
    }
  
    .input-label {
      display: block;
      margin-bottom: 5px;
      font-weight: 500;
    }
  
    .input {
      width: 100%;
      padding: 10px;
      border: 1px solid #ced4da;
      border-radius: 4px;
    }
  
    .button {
      width: 100%;
      padding: 10px;
      background-color: #007bff;
      border: none;
      color: white;
      font-size: 16px;
      border-radius: 4px;
      cursor: pointer;
    }
  
    .button:hover {
      background-color: #0056b3;
    }
  
    .faint-text {
      text-align: center;
      margin-top: 20px;
    }
  
    .faint-text a {
      color: #007bff;
      text-decoration: none;
    }
  
    .faint-text a:hover {
      text-decoration: underline;
    }
</style>
  
<div class="page-wrapper">
  <div class="section_half-half">
    <div class="half-width">
      <a href="#" class="navbar_logo-link w-nav-brand">

        <div class="logotxt" on:click="{() => navigate('/home')}">거대<span class="text-brand" on:click="{() => navigate('/home')}">박격포</span></div>
      </a>
      <form id="wf-form-signup" name="wf-form-signup" data-name="signup" method="get" data-ms-form="signup"
            class="form-container" on:submit={signup}>
        <h1 class="h1-small">Create an account</h1>
        <div class="input-wrapper">
          <label for="First-Name-4" class="input-label">아이디</label>
          <input class="input" maxlength="256"
                  type="text" bind:value={username} required />
        </div>
        <div class="input-wrapper">
          <label for="Password-4" class="input-label">비밀번호</label>
          <input class="input" maxlength="256" 
                  type="password" bind:value={password} required />
        </div>
        <div class="input-wrapper">
          <label for="Last-Name-4" class="input-label">Affiliation</label>
          <input class="input" maxlength="256" 
                 type="text" bind:value={affiliation} required />
        </div>
        
        <br>
        <select bind:value={usergroup} >
          <option value="" disabled selected>Select user type</option>
          <option value="1">Employer</option>
          <option value="2">Applicant</option>
        </select>
        <br><br>

        <input type="submit" class="button" value="Sign Up" />
      </form>
      <div class="faint-text">
        <div>Have an account?
          <a href="#" on:click="{() => navigate('/login')}">Sign In
          </a>
        </div>
      </div>
      <div>Copyright ? 2022 My Company.</div>
    </div>
    <div class="half-width" style="background-color: green;">
      <!-- Optional content for the second half, like an image or additional information -->
    </div>
  </div>
</div>
  
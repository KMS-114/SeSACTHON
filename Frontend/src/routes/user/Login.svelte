<script>
  import { navigate } from 'svelte-routing';
  import { writable } from 'svelte/store';
  import { isLoggedIn, user, userType } from '../../lib/store';

  let username = '';
  let password = '';
  let usergroup;
  let currentUser;

  async function login(event) {
    event.preventDefault(username);
    const response = await fetch(`http://localhost:8000/user/get/${username}`);
      if (!response.ok) {
        throw new Error('로그인에 실패했습니다');
      }
    if (response.ok) {
      const data = await response.json();
      usergroup = data.userGroup;
      currentUser = data.username;
      console.log('login', data);

      isLoggedIn.set(true);
      user.set(currentUser);
      userType.set(usergroup);
      localStorage.setItem('token', data.access_token);


      console.log('current ', currentUser);
      console.log('setting ', user);

      alert('Login successful');
      if (usergroup === 1) {
        navigate('/home', { replace: true });
      } else if (usergroup === 2) {
        navigate('/home', { replace: true });
      } else {
        navigate('/', { replace: true });
      }
    } else {
      alert('Login failed');
    }
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
    position: fixed;
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
  .select{
    padding: 10px;
  }
</style>

<div class="page-wrapper">
  <div class="section_half-half">
    <div class="half-width">
      <a href="#" class="navbar_logo-link w-nav-brand">
        <div class="logotxt" on:click="{() => navigate('/home')}">거대<span class="text-brand" on:click="{() => navigate('/home')}">박격포</span></div>
      </a>
      <form id="wf-form-signup" name="wf-form-signup" data-name="signup" method="get" data-ms-form="login"
            class="form-container" on:submit={login}>
        <h1 class="h1-small">Login</h1>
        <div class="input-wrapper">
          <label class="input-label">아이디</label>
          <input class="input" maxlength="256"
                 type="text" bind:value={username} required />
        </div>
        <div class="input-wrapper">
          <label class="input-label">비밀번호</label>
          <input class="input" maxlength="256"
                 type="password" bind:value={password} required />
        </div>
        <!-- <select bind:value={userGroup}>
          <option value="" disabled selected>Select user type</option>
          <option value="1">Employer</option>
          <option value="2">Applicant</option>
        </select>
        <br><br> -->

        <input type="submit" class="button" value="Log In" />
      </form>
      <div class="faint-text">
        <div>Need an account?
          <a href="#" on:click="{() => navigate('/signup')}">Sing up
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

<script>
  import { navigate } from 'svelte-routing';
  import { writable } from 'svelte/store';

  let email = '';
  let password = '';

  async function login(event) {
    event.preventDefault();
    const response = await fetch('http://localhost:8000/user/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({
        'username': email,
        'password': password,
      }),
    });

    if (response.ok) {
      const data = await response.json();
      localStorage.setItem('token', data.access_token);
      alert('Login successful');
      navigate('/home', { replace: true });
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
          <label for="Email-5" class="input-label">Email</label>
          <input class="input" maxlength="256" name="Email-5" data-name="Email 5"
                 placeholder="e.g. howard.thurman@gmail.com" type="email" bind:value={email} required />
        </div>
        <div class="input-wrapper">
          <label for="Password-4" class="input-label">Password</label>
          <input class="input" maxlength="256" name="Password-4" data-name="Password 4" placeholder=""
                 type="password" bind:value={password} required />
        </div>
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

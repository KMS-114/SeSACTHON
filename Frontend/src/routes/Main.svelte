<script>
  import { navigate } from 'svelte-routing';
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Amatic+SC');

html, body {
  margin: 0;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-image: linear-gradient(to top, #d9afd9 0%, #97d9e1 100%);
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
}

.container {
  text-align: center;
}

.button_container {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.description, .link {
  font-family: 'Amatic SC', cursive;
  text-align: center;
  font-size: 150px;
}

.subdescription {
  font-family: 'Amatic SC', cursive;
  text-align: center;
  font-size: 40px;
}

.btn {
  border: none;
  text-align: center;
  cursor: pointer;
  text-transform: uppercase;
  outline: none;
  overflow: hidden;
  position: relative;
  color: #fff;
  font-weight: 700;
  font-size: 15px;
  background-color: #222;
  padding: 17px 60px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.20);
}

.btn span {
  position: relative; 
  z-index: 1;
}

.btn:after {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  height: 490%;
  width: 140%;
  background: #78c7d2;
  transition: all .5s ease-in-out;
  transform: translateX(-98%) translateY(-25%) rotate(45deg);
}

.btn:hover:after {
  transform: translateX(-9%) translateY(-25%) rotate(45deg);
}

.link {
  font-size: 20px;
  margin-top: 30px;
}

.link a {
  color: #000;
  font-size: 25px; 
}
</style>
<body>
<div class="container">
  <p class="description">CHIUP</p>
  <p class="subdescription">사회적 약자를 위한 채용 플랫폼</p>
  <div class="button_container">
    <button class="btn" on:click={() => navigate('/login')}><span>Login</span></button>
    <button class="btn" on:click={() => navigate('/signup')}><span>Signup</span></button>
  </div>
</div>
</body>
<script>
    import { navigate } from 'svelte-routing';
    import Navbar from '../components/Navbar.svelte';
</script>

<Navbar />

<style>
  body {
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
  h1{
    text-align: center;
  }
  .container{
    text-align: center;
  }
  .description{
    font-family: 'Amatic SC', cursive;
    text-align: center;
    font-size: 150px;
  }
</style>

<body>
  <div class="container">
    <p class="description">거대 박격포.</p>
  </div>
</body>
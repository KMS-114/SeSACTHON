<script>
    import { navigate } from 'svelte-routing';
    import Navbar from '../components/Navbar.svelte';
    import { user, userType } from '../lib/store';

    let currentUser = '';
    let currentUserType = '';

    user.subscribe(value => {
      currentUser = value;
    });

    userType.subscribe(value => {
      currentUserType = value;
    });

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
  .subdescription{
    font-family: 'Amatic SC', cursive;
    text-align: center;
    font-size: 50px;
  }
  .content{
    font-family: 'Amatic SC', cursive;
    text-align: center;
    font-size: 30px;
  }

</style>

<body>
  <div class="container">
    <p class="description">박 격 포</p>
    <p class="subdescription">사회적 약자를 위한 채용 플랫폼</p>
    <p class="content">반갑습니다. </p>
    <p class="content">{currentUser}
      {#if currentUserType == '1'}
        공고주님
      {/if}
      {#if currentUserType == '2'}
        지원자님
      {/if}</p>




  </div>
</body>
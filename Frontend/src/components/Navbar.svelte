<script>
  import { navigate } from 'svelte-routing';
  import { isLoggedIn, user, userType } from '../lib/store';

  let loggedIn = false;
  let currentUser;
  let currentUserType;

  isLoggedIn.subscribe(value => {
    loggedIn = value;
  });

  user.subscribe(value => {
    currentUser = value;
  });

  userType.subscribe(value => {
    currentUserType = value;
  });

  function handleLogout() {
    isLoggedIn.set(false);
    user.set(null);
    userType.set(null);
    localStorage.removeItem('token');
    navigate('/');
  }
</script>
  
<nav>
  <div class="nav-container">
    <ul class="menu">
        <a href="#" class="nav-link" on:click="{() => navigate('/home')}">Home</a>
        <a href="#" class="nav-link" on:click="{() => navigate('/jobpostlist')}">채용 공고</a>
        {#if currentUserType=="1"}
          <a href="#" class="nav-link" on:click="{() => navigate('/myjobpostlist')}">나의 공고</a>
        {/if}
        {#if currentUserType=="2"}
          <a href="#" class="nav-link" on:click="{() => navigate('/myresume')}">나의 이력서</a>
          <a href="#" class="nav-link" on:click="{() => navigate('/profile')}">프로필 작성</a>
        {/if}
        <a href="#" class="nav-link" on:click="{() => navigate('/myInfo')}">나의 정보</a>
    </ul>
    <div class="button-group">
      {#if loggedIn}
        <button type="button" class="btn btn-outline-light" on:click={handleLogout}>Logout</button>
      {:else}
      <!-- <button type="button" class="btn btn-outline-light" on:click={() => navigate('/login')}>Login</button>
      <button type="button" class="btn btn-warning" on:click={() => navigate('/signup')}>Signup</button> -->
      {/if}

    </div>
  </div>
</nav>
  
<style>
  nav {
    background-color: #333;
    padding: 1rem;
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;
  }

  .nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .menu {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    gap: 2rem; /* 링크 사이의 간격 */
  }

  .nav-link {
    color: white; /* 글자 색상 변경 */
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    font-family: Arial, sans-serif;
    font-size: 24px; /* 글자 크기 변경 */
    transition: background-color 0.3s ease, color 0.3s ease;
  }

  .nav-link:hover {
    background-color: #555;
    color: #ffeb3b; /* hover 상태에서도 변경된 글자 색상 유지 */
  }

  .nav-link.active {
    background-color: #111;
    color: #ffeb3b; /* active 상태에서도 변경된 글자 색상 유지 */
  }

  .button-group {
    display: flex;
    gap: 1rem; /* 버튼 사이의 간격 */
  }

  .btn {
    padding: 0.5rem 1rem;
    font-size: 20px; /* 버튼 글자 크기 변경 */
  }

  .btn-outline-light {
    color: black; /* 버튼 글자 색상 변경 */
    border-color: #ffeb3b; /* 버튼 테두리 색상 변경 */
  }

  .btn-outline-light:hover {
    background-color: #ffeb3b; /* hover 상태에서 버튼 배경 색상 변경 */
    color: #333; /* hover 상태에서 버튼 글자 색상 변경 */
  }

  .btn-warning {
    background-color: #ffeb3b; /* 버튼 배경 색상 변경 */
    color: #333; /* 버튼 글자 색상 변경 */
    border-color: #ffeb3b; /* 버튼 테두리 색상 변경 */
  }

  .btn-warning:hover {
    background-color: #fff176; /* hover 상태에서 버튼 배경 색상 변경 */
    color: #333; /* hover 상태에서 버튼 글자 색상 변경 */
  }
</style>

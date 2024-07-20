<script>
  import { navigate } from 'svelte-routing';
  import { onMount } from 'svelte';
  import Navbar from '../../components/Navbar.svelte';
  import { isLoggedIn, user, userType } from '../../lib/store';

  let username = '';
  let password = '';
  let usergroup;
  let currentUser;
  let affiliation;
  let createdAt;
  let error = null;



  async function fetchMyInfo() {
    try{
      console.log('current', currentUser);
      const response = await fetch(`http://localhost:8000/user/get/${currentUser}`);
      if (!response.ok) {
        throw new Error('네트워크 오류 실패했습니다');
      }
      else{
        const data = await response.json();
        usergroup = data.userGroup;
        currentUser = data.username;
        affiliation = data.affiliation;
        createdAt = data.createdAt;

        console.log('setting finish ', currentUser);

      }
    }catch(err){
      error = err.message;
      console.log(error);
    }
  }
  // 컴포넌트가 마운트될 때 fetchMyInfo 호출
  onMount(() => {

    // user 스토어 구독
    user.subscribe(value => {
      currentUser = value;
      fetchMyInfo();
    });

    // userType 스토어 구독
    userType.subscribe(value => {
      usergroup = value;
    });

    fetchMyInfo();

  });

  // 계정 삭제
  async function deleteUser() {
    try {
      const response = await fetch(`http://localhost:8000/user/drop/${currentUser}`);
      if (!response.ok) {
        throw new Error('사용자 삭제 실패했습니다');
      } else {
        // 사용자 삭제 후 로그아웃 또는 다른 페이지로 이동
        navigate('/login');
      }
    } catch (err) {
      error = err.message;
      console.log(error);
    }
  }
</script>

<Navbar />

<main class="container">
  {#if error}
    <p class="error">{error}</p>
  {:else}
    <div class="job-detail">
      <p><strong>아이디 : </strong> {currentUser}</p>
      <p><strong>형태 : </strong>
        {#if usergroup == 1}
          공고주  
        {/if}
        {#if usergroup == 2}
          지원자  
        {/if}
      <p><strong>학력 : </strong> {affiliation}</p>
      <p><strong>생성 날짜 : </strong> {createdAt}</p>
      <div class="apply-btn-container">
        <button class="apply-btn" on:click={deleteUser}><span>삭제하기</span></button>
      </div>
    </div>
  {/if}
</main>

<style>
  main {
    font-family: Arial, sans-serif;
    padding: 20px;
    font-size: 18px;
  }
  .container {
    max-width: 1600px;
    max-height: 1800px;
    margin: 0 auto;
    padding: 20px;
  }

  .job-detail {
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-top: 20px;
    position: relative;
  }

  .job-detail h1 {
    margin-top: 0;
    color: #333;
  }

  .job-detail p {
    color: #555;
    line-height: 1.6;
  }

  .job-detail p strong {
    color: #000;
  }


  .error {
    color: red;
    text-align: center;
  }
  .apply-btn-container {
    display: flex;
    justify-content: flex-end;
    margin-top: 20px;
  }

  .apply-btn {
    align-self: flex-end; /* 버튼을 우측 끝에 정렬 */
    padding: 10px 20px;
    font-size: 16px;
    color: #fff;
    background-color: #007bff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  .apply-btn:hover {
    background-color: #0056b3;
  }
</style>

<script>
  import { onMount } from 'svelte';
  import { navigate } from 'svelte-routing'; // 라우터 임포트
  import Navbar from '../../components/Navbar.svelte';
  import { user, userType } from '../../lib/store';
  import JobDetail from './JobDetail.svelte';

  let currentUser;
  let currentUserType;

  let jobListings = [];
  let filteredJobListings = [];
  let error = null;

  async function fetchJobListings() {
    try {
      const response = await fetch('http://localhost:8000/job_posting/all/');
      if (!response.ok) {
        throw new Error('네트워크 응답이 실패했습니다');
      }
      const data = await response.json();
      // console.log(data)
      if (!Array.isArray(data.jobPostings)) {
        throw new Error('API 응답이 배열이 아닙니다.');
      }
      jobListings = data.jobPostings;
      filterJobs();
      console.log('user : ', currentUser);
      console.log('job', filteredJobListings);
    } catch (err) {
      error = err.message;
    }
  }
  function filterJobs() {
    filteredJobListings = jobListings.filter(job => {
      const matchesUser = job.username === currentUser;
      console.log(`Job username: ${job.username}, Current userID: ${currentUser}, Matches: ${matchesUser}`);
      return matchesUser;
    });
  }

  onMount(() => {
    try{
        // user 스토어 구독
      user.subscribe(value => {
        currentUser = value;
      });

      // userType 스토어 구독
      userType.subscribe(value => {
        currentUserType = value;
      });

      fetchJobListings();

    } catch (err) {
      error = err.message;
      console.log(error);
    }
  });

  function selectJob(job) {
      navigate(`/applyuserlist/${job.id}`);
  }
</script>
<Navbar />

<main class="container">
<br><br><br><br>
<h1>나의 채용 공고들</h1>
{#if error}
  <p class="error">{error}</p>
{:else}
  <ul class="job-list">
    {#each filteredJobListings as job}
      <li class="job-item" on:click={() => selectJob(job)}>
        <h2>{job.title}</h2>
        <p><strong>설명:</strong> {job.description}</p>
      </li>
    {/each}
  </ul>
{/if}
</main>

<style>
@import url('https://fonts.googleapis.com/css?family=Amatic+SC');
.header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 20px;
}
.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'LotteMartDream', sans-serif;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}

.search-filter {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.search-filter input,
.search-filter select {
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.search-filter select {
  width: 200px;
}

.error {
  color: red;
  text-align: center;
}

.job-list {
  list-style-type: none;
  padding: 0;
}

.job-item {
  background: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  transition: background 0.3s, box-shadow 0.3s;
  cursor: pointer;
}

.job-item:hover {
  background: #f1f1f1;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h2 {
  margin-top: 0;
  color: #007BFF;
}

p {
  margin: 5px 0;
  color: #555;
}

p strong {
  color: #333;
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

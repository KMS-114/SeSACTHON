<script>
    import { onMount } from 'svelte';
    import { navigate } from 'svelte-routing'; // 라우터 임포트
    import Navbar from '../../components/Navbar.svelte';
    import { user, userType } from '../../lib/store';
    import JobDetail from './JobDetail.svelte';

    let currentUser;
    let currentUserType;

    user.subscribe(value => {
      currentUser = value;
    });

    userType.subscribe(value => {
      currentUserType = value;
    });

    let jobListings = [];
    let filteredJobListings = [];
    let error = null;
    let searchQuery = '';
    let filterCompany = '';
  
    async function fetchJobListings() {
    try {
      const response = await fetch('http://localhost:8000/job_posting/all/');
      if (!response.ok) {
        throw new Error('네트워크 응답이 실패했습니다');
      }
      const data = await response.json();
      console.log(data)
      if (!Array.isArray(data.jobPostings)) {
        throw new Error('API 응답이 배열이 아닙니다.');
      }
      jobListings = data.jobPostings;
      filteredJobListings = jobListings;
      console.log(filteredJobListings);
    } catch (err) {
      error = err.message;
    }
  }
    function filterJobs() {
      const query = searchQuery.toLowerCase();
      
      filteredJobListings = jobListings.filter(job => {
      const matchesQuery = job.title.toLowerCase().includes(query) || job.description.toLowerCase().includes(query);
      console.log(`Job username: ${job.username}, job title : ${job.title}`);
      return matchesQuery;
      });
    }

    onMount(fetchJobListings);

    function selectJob(job) {
      navigate(`/jobdetail/${job.id}`);
    }
</script>
<Navbar />

<main class="container">
  <br><br><br><br>
  <h1>채용 공고 리스트</h1>
  <div class="header">
    {#if currentUserType == "1"}
      <div class="apply-btn-container">
        <button class="apply-btn" on:click={() => navigate('/jobpost')}><span>공고 작성</span></button>
      </div>
    {/if}
  </div>
  <div class="search-filter">
    <input type="text" placeholder="검색어 입력" bind:value={searchQuery} on:input={filterJobs} />
    <select bind:value={filterCompany} on:change={filterJobs}>
      <option value="">모든 공고</option>
      {#each [...new Set(jobListings.map(job => job.title))] as title}
        <option value={title}>{title}</option>
      {/each}
    </select>
  </div>
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
  
<script>
  import { onMount } from 'svelte';
  import { navigate, Link } from 'svelte-routing';
  import Navbar from '../../components/Navbar.svelte';
  import { userType } from '../../lib/store';

  let currentUserType;

  userType.subscribe(value => {
    currentUserType = value;
  });

  function getIdFromPath() {
    const path = window.location.pathname;
    const segments = path.split('/');
    return segments[segments.length - 1];
  }
  let id = null;
  let job = null;
  let error = null;

  // This part is used when job is not provided as a prop
  async function fetchJobDetail(id) {
    try {
      const response = await fetch(`http://localhost:8000/job-listings/${id}`);
      if (!response.ok) {
        throw new Error('네트워크 응답이 실패했습니다');
      }
      job = await response.json();
    } catch (err) {
      error = err.message;
    }
  }

  // Fetch job detail if job is not passed as a prop
  onMount(() => {
    try{
      id = getIdFromPath();
      console.log('Job ID:', id);
      if (!job) {
        fetchJobDetail(id);
      }
    } catch (err) {
      error = err.message;
    }
  });

  function selectJob(job) {
      navigate(`/applyjob/${job.id}`);
    }
</script>

<Navbar />
<main class="container">
  {#if error}
    <p class="error">{error}</p>
  {:else}
    {#if job}
      <div class="job-detail">
        <h1>{job.title}</h1>
        <p><strong>회사:</strong> {job.company}</p>
        <p><strong>설명:</strong> {job.description}</p>
        <!-- <p><strong>위치:</strong> {job.location}</p>
        <p><strong>급여:</strong> {job.salary}</p>
        <p><strong>게시일:</strong> {job.postedDate}</p> -->
        {#if currentUserType=="2"}
          <div class="apply-btn-container">
            <button class="apply-btn" on:click={() => selectJob(job)}>지원하기</button>
          </div>
        {/if}
      </div>
    {/if}
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

  .apply-btn-container {
    display: flex;
    justify-content: flex-end;
    margin-top: 20px;
  }

  .apply-btn {
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

  .error {
    color: red;
    text-align: center;
  }
</style>
<script>
  import { onMount } from 'svelte';
  import { navigate, Link } from 'svelte-routing';
  import Navbar from '../../components/Navbar.svelte';
  import { userType } from '../../lib/store';

  const timestamp = new Date().toISOString();

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

  let title = '';
  let description = '';
  let ageMin = 0;
  let ageMax = 0;
  let additionalProp1 = '';
  let additionalProp2 = '';
  let additionalProp3 = '';

  let createdAt = timestamp;

  // This part is used when job is not provided as a prop
  async function fetchJobDetail(id) {
    try {
      const response = await fetch(`http://localhost:8000/job_posting/detail/${id}`);
      if (!response.ok) {
        throw new Error('네트워크 응답이 실패했습니다');
      }
      job = await response.json();
      console.log('job ',job);
      title = job.title;
      description = job.description;
      ageMin = job.qualificationsRequired.ageMin;
      ageMax = job.qualificationsRequired.ageMax;
      createdAt = job.createdAt;
      additionalProp1 = job.qualificationsRequired.customQualification.additionalProp1;
      additionalProp2 = job.qualificationsRequired.customQualification.additionalProp2;
      additionalProp3 = job.qualificationsRequired.customQualification.additionalProp3;
      console.log('job title',title);

    } catch (err) {
      error = err.message;
      console.log(error);
    }
  }

  // Fetch job detail if job is not passed as a prop
  onMount(() => {
    try{
      id = getIdFromPath();
      if (id != null) {
        console.log('Get Job ID:', id);

        fetchJobDetail(id);
      }
    } catch (err) {
      error = err.message;
      console.log(error);
    }
  });

  function applyJob() {
      console.log('post to apply Job ID:', id);
      navigate(`/applyjob/${id}`);
    }
</script>

<Navbar />

<main class="container">
  {#if error}
    <p class="error">{error}</p>
  {:else}
    <div class="job-detail">
      <h2>{title}</h2>
      <p><strong>설명 : </strong> {description}</p>
      <p><strong>최소 나이 : </strong> {ageMin}  
        <strong>최대 나이 : </strong> {ageMax} </p>
      <p><strong>자격증 : </strong> {additionalProp1}, {additionalProp2}, {additionalProp3}</p>
      <p><strong>작성일 : </strong> {createdAt}</p>

      {#if currentUserType=="2"}
        <div class="apply-btn-container">
          <button class="apply-btn" on:click={() => applyJob()}>지원하기</button>
        </div>
      {/if}
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
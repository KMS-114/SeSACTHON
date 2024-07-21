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
      title = job.title;
      description = job.description;
      ageMin = job.qualificationsRequired.ageMin;
      ageMax = job.qualificationsRequired.ageMax;
      createdAt = job.createdAt;
      additionalProp1 = job.qualificationsRequired.customQualification.additionalProp1;
      additionalProp2 = job.qualificationsRequired.customQualification.additionalProp2;
      additionalProp3 = job.qualificationsRequired.customQualification.additionalProp3;
      // console.log('job title',title);

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
        fetchResumeListings(id);
      }
    } catch (err) {
      error = err.message;
      console.log(error);
    }
  });


  // 해당 공고 지원자 정보 받아오기
  let resumeListings = [];
  let filteredResumeListings = [];

  async function fetchResumeListings(id) {
    try {
      const response = await fetch('http://localhost:8000/resume/all/');
      if (!response.ok) {
        throw new Error('네트워크 응답이 실패했습니다');
      }
      const data = await response.json();
      // console.log(data)
      if (!Array.isArray(data.resumes)) {
        throw new Error('API 응답이 배열이 아닙니다.');
      }
      resumeListings = data.resumes;

      filterResumes(id);
      console.log('final resume : ',filteredResumeListings);

    } catch (err) {
      error = err.message;
    }
  }
  function filterResumes(id) {
    filteredResumeListings = resumeListings.filter(resume => {
      const matchesUser = resume.jobPostingId === id;
      return matchesUser;
    });
  }
  
</script>

<Navbar />

<main class="container">
  {#if error}
    <p class="error">{error}</p>
  {:else}
    <div class="job-detail">
      <div class="one">
        <h1>채용 공고 설명</h1>
      </div>
      <h2>{title}</h2>
      <p><strong>설명 : </strong> {description}</p>
      <p><strong>최소 나이 : </strong> {ageMin}  
        <strong>최대 나이 : </strong> {ageMax} </p>
      <p><strong>자격증 : </strong> {additionalProp1}, {additionalProp2}, {additionalProp3}</p>
      <p><strong>작성일 : </strong> {createdAt}</p>

    </div>
    <br>
    <div class="one">
      <h1>지원자 목록</h1>
    </div>
    <ul class="job-list">

      {#each filteredResumeListings as resume}
        <li class="job-item">
          <h2>{resume.username}</h2>
          <div class="apply-btn-container">
            <button class="apply-btn" on:click={() => applyJob()}>가상 면접</button>
          </div>
        </li>
      {/each}
    </ul>
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
h1 {
  position: relative;
  padding: 0;
  margin: 0;
  font-family: "Raleway", sans-serif;
  font-weight: 300;
  font-size: 40px;
  color: #080808;
  -webkit-transition: all 0.4s ease 0s;
  -o-transition: all 0.4s ease 0s;
  transition: all 0.4s ease 0s;
}

h1 span {
  display: block;
  font-size: 0.5em;
  line-height: 1.3;
}
h1 em {
  font-style: normal;
  font-weight: 600;
}

/* === HEADING STYLE #1 === */
.one h1 {
  text-align: center;
  text-transform: uppercase;
  padding-bottom: 5px;
}
.one h1:before {
  width: 28px;
  height: 5px;
  display: block;
  content: "";
  position: absolute;
  bottom: 3px;
  left: 50%;
  margin-left: -14px;
  background-color: #b80000;
}
.one h1:after {
  width: 100px;
  height: 1px;
  display: block;
  content: "";
  position: relative;
  margin-top: 25px;
  left: 50%;
  margin-left: -50px;
  background-color: #b80000;
}

</style>
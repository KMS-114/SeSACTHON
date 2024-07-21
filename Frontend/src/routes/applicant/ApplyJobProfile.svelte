<script>
  import { onMount } from 'svelte';
  import { navigate, Link } from 'svelte-routing';
  import Navbar from '../../components/Navbar.svelte';
  import '@fortawesome/fontawesome-free/css/all.css';
  import { user, userType } from '../../lib/store';

  const timestamp = new Date().toISOString();

  let currentUserType;
  let currentUser;

  function getIdFromPath() {
    const path = window.location.pathname;
    const segments = path.split('/');
    return segments[segments.length - 1];
  }

  // ================= 공고 정보 ===============================

  let jobid = null;
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
  let coverLetterQuestions = [];

  // let alertMessage = '';

  // 해당 공고 정보 받아오기
  async function fetchJobDetail(jobid) {
    try {
      const response = await fetch(`http://localhost:8000/job_posting/detail/${jobid}`);
      if (!response.ok) {
        throw new Error('네트워크 응답이 실패했습니다');
      }
      job = await response.json();
      // console.log('job ',job);
      title = job.title;
      description = job.description;
      ageMin = job.qualificationsRequired.ageMin;
      ageMax = job.qualificationsRequired.ageMax;
      createdAt = job.createdAt;
      additionalProp1 = job.qualificationsRequired.customQualification.additionalProp1;
      additionalProp2 = job.qualificationsRequired.customQualification.additionalProp2;
      additionalProp3 = job.qualificationsRequired.customQualification.additionalProp3;
      coverLetterQuestions = job.coverLetterQuestions;
      initializeUserAnswers();

      // console.log('job title',coverLetterQuestions);

    } catch (err) {
      error = err.message;
      console.log(error);
    }
  }


  // ===================== 지원자 정보 ==========================
  let userName = '';
  let userBirth = '';
  let userGender = 1;
  let userProp1 = '';
  let userProp2 = '';
  let userProp3 = '';
  let userSkills = [];
  let userCareers = [];

  let profileLists = [];
  let filterprofileLists = [];


  let userCoverLetters = [];

  function initializeUserAnswers() {
    userCoverLetters = coverLetterQuestions.map(question => ({
      questionId: question.coverLetterQuestionId,
      answer: ''
    }));
    // console.log('Initialized userCoverLetters:', userCoverLetters); // 콘솔 로그로 초기화 확인
  }
  let alertMessage = '';


  // 지원자의 정보 가져오기
  async function fetchUserProfile() {
    try {
      const response = await fetch(`http://localhost:8000/profile/all`);
      if (!response.ok) {
        throw new Error('네트워크 응답이 실패했습니다');
      }
      const data = await response.json();
      profileLists = data.profiles;

      filterUserProfile();
      console.log('profile',filterprofileLists[0]);

      userName = filterprofileLists[0].name;
      userBirth = formatDate(filterprofileLists[0].birth);
      userGender = filterprofileLists[0].gender;
      userSkills = filterprofileLists[0].skills;
      // userCareers = filterprofileLists[0].careers;
      userCareers = filterprofileLists[0].careers.map(career => ({
        ...career,
        startDate: formatDate(career.startDate),
        endDate: formatDate(career.endDate)
      }));


    } catch (err) {
      error = err.message;
      console.log(error);
    }
  }
  function filterUserProfile() {
    filterprofileLists = profileLists.filter(profile => {
      const matchesUser = profile.username === currentUser;
      return matchesUser;
    });
  }

  function formatDate(dateString) {
    return dateString.split('T')[0];
  }

  
  function handleRadioChange(event) {
    userGender = event.target.value;
    console.log("Selected gender:", userGender);
  }

  // 공고 정보 및 지원자 정보 가져오기
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


      fetchUserProfile();

      jobid = getIdFromPath();
      if (jobid != null) {
        fetchJobDetail(jobid);
      }
      // 지원자 정보
      // if (userid != null){

      // }
    } catch (err) {
      error = err.message;
      console.log(error);
    }
  });


  function fillResume() {
    console.log('post to apply Job ID:', jobid);
    navigate(`/applyjob/${jobid}`);
  }

function updateAnswer(index, value) {
    userCoverLetters = userCoverLetters.map((item, i) =>
      i === index ? { ...item, answer: value } : item
    );
  }

</script>

<Navbar />

<main class="container">
  <br><br><br><br><br><br>
  <h1>{job?.title} 이력서 작성</h1>
  <h4>(프로필 및 기본 인적사항 작성)</h4>
  <br><br>
  
  <form on:click={() => fillResume()}>
    <fieldset>
      <label>이름</label>
      <input type="text" bind:value={userName}/>

      <label>
        생년월일:
        <input type="date" bind:value={userBirth} />
      </label>

      <div class="radio-group">
        <label>남자<input type="radio" name="userGender" value=1 bind:group={userGender} on:change={handleRadioChange} />
        </label>
        <label>여자<input type="radio" name="userGender" value=2 bind:group={userGender} on:change={handleRadioChange} />
        </label>
      </div>

      <label>학력</label>
      <input type="text" bind:value={userProp1} />
      <label>자격증</label>
      <input type="text" bind:value={userProp2} />
      <!-- <label>경력</label>
      <input type="text" bind:value={userProp3} /> -->
    </fieldset>

    <fieldset>
      <legend>기술</legend>
      {#each userSkills as skill, index}
        <label> 기술 {index + 1}:</label>
          <br>
          <div>
              <input type="text" bind:value={userSkills[index]} placeholder="프로그래밍" required />
          </div>
      {/each}
      <br>
    </fieldset>
  
    <fieldset>
      <legend>경력 사항</legend>
      {#each userCareers as career, index}
        <br>
        <div>
            <label>시작 날짜:</label>
            <input type="date" bind:value={career.startDate} required />

            <label>종료 날짜:</label>
            <input type="date" bind:value={career.endDate} />

            <label>소속:</label>
            <input type="text" bind:value={career.affiliation} required />

            <label>요약:</label>
            <textarea bind:value={career.summary} required></textarea>
        </div>
      {/each}
      <br>
    </fieldset>
    
    <button type="submit">다음</button>
  </form>

</main>


<style>
  .record-button {
    background: none;
    border: none;
    cursor: pointer;
    font-size: 1.2em;
    color: #007bff;
  }

  .record-button .fas {
    margin-right: 5px;
  }

  .record-button:hover {
    color: #0056b3;
  }
.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'LotteMartDream', sans-serif;
}

h1 {
    text-align: center;
    margin-bottom: 20px;
    color: #333;
}

.alert {
    color: green;
    margin: 20px 0;
    text-align: center;
}

form {
    display: flex;
    flex-direction: column;
}

label {
    margin-bottom: 10px;
    font-weight: bold;
    color: #333;
}

input, textarea {
    padding: 10px;
    font-size: 1rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    margin-bottom: 20px;
    width: 100%;
}

textarea {
    resize: vertical;
    height: 100px;
}

button {
    padding: 10px 20px;
    font-size: 1rem;
    border: none;
    border-radius: 4px;
    background-color: #007BFF;
    color: white;
    cursor: pointer;
    transition: background 0.3s;
}

button:hover {
    background-color: #0056b3;
}
.radio-group {
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
    align-items: center;
    margin-left: 320px;
  }
  legend{
    font-weight: bold;
    font-size: 1.2em; /* 글자 크기 조절 */
    color:green;
  }
</style>
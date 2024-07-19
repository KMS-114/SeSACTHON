<script>
  import { navigate } from 'svelte-routing';
  import Navbar from '../../components/Navbar.svelte';
  import '@fortawesome/fontawesome-free/css/all.css';

  let userId = '6695199d04cbd3e40f64419a'; // 필요시 실제 유저 ID로 설정
  let title = '';
  let description = '';
  
  let qualificationsRequired = {
    ageMin: '',
    ageMax: '',
    gender: '',
    customQualification: {
          affiliation: '',
          career:''
        }
  };
    
  let coverLetterQuestions = [];

  let content = '';
  let charLimit = '';

  function addQuestion() {
    coverLetterQuestions = [...coverLetterQuestions, { content: '', charLimit: 500 }];
  }

  let alertMessage = '';

  async function handleJobPosting() {
    const timestamp = new Date().toISOString();

    const jobPostingData = {
      userId,
      title,
      description,
      qualificationsRequired,
      coverLetterQuestions,
      createdAt: timestamp,
      updatedAt: timestamp
    };
    

    try {
      const response = await fetch('http://localhost:8000/job_posting/create/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
      },
        body: JSON.stringify(jobPostingData)
      });

      if (response.ok) {
        alertMessage = '채용 공고가 성공적으로 작성되었습니다.';
        // Clear form fields
        title = '';
        description = '';
        qualificationsRequired = {
          ageMin: '',
          ageMax: '',
          gender: '',
          customQualification: {
            affiliation: '',
            career: ''
          }
        };
        coverLetterQuestions = [];
        
        setTimeout(() => {
          alertMessage = '';
          navigate('/'); // 변경된 경로 설정
        }, 2000); // 2초 후에 채용 공고 리스트 페이지로 이동
      } else {
        const result = await response.json();
        alertMessage = `작성 실패: ${result.detail}`;
      }
    } catch (error) {
      alertMessage = `작성 실패: 서버 오류 - ${error.message}`;
    }
  }

</script>

<Navbar />

<main class="container">
  <br><br><br><br>
  {#if alertMessage}
    <div class="alert">{alertMessage}</div>
  {/if}
  <h1>채용 공고 작성</h1>
  <form on:submit|preventDefault={handleJobPosting}>
    <label>주제</label>
    <input type="text" bind:value={title} required />

    <label>설명:</label>
    <textarea bind:value={description} required></textarea>

    <fieldset>
      <!-- <legend>자격 요건</legend> -->
      <label>최소 나이:</label>
      <input type="number" bind:value={qualificationsRequired.ageMin} required />

      <label>최대 나이</label>
      <input type="number" bind:value={qualificationsRequired.ageMax} required />

      <label>성별</label>
      <select bind:value={qualificationsRequired.gender} required>
        <option value="" disabled selected>선택</option>
        <option value="1">남성</option>
        <option value="2">여성</option>
      </select>

      <label>학력</label>
      <input type="text" bind:value={qualificationsRequired.customQualification.affiliation} required />

      <label>경력</label>
      <input type="text" bind:value={qualificationsRequired.customQualification.career} required />
    </fieldset>

    <fieldset>
      <legend>자기소개서 질문</legend>
      <br>
      {#each coverLetterQuestions as question, index}
        <div>
          <br>
          <label>질문 {index + 1}:</label>
          <input type="text" bind:value={question.content} required />
          <button type="button" on:click={() => removeQuestion(index)}>질문 삭제</button>
        </div>
      {/each}
      <br>
      <button type="button" on:click={addQuestion}>질문 추가</button>
    </fieldset>
    <br><br>
    <button type="submit">작성</button>
  </form>
</main>
<style>
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
</style>
  
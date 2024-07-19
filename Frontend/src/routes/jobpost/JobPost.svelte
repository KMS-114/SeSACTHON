<script>
  import { navigate } from 'svelte-routing';
  import Navbar from '../../components/Navbar.svelte';
  import '@fortawesome/fontawesome-free/css/all.css';

  let title = '';
  let description = '';
  let company = '';
  
  let qualificationsRequired = {
    ageMin: '',
    ageMax: '',
    gender: ''
  }
  let customQualification = {
          affiliation: '',
          career:''
        }
    

  let coverLetterQuestions = {
    content: '',
        username: '',
        charLimit: '',
        affiliation: '',
        createdAt: '',
        updatedAt: ''
    };


  let alertMessage = '';

  async function handleJobPosting() {
    const formData = new FormData();
    
    formData.append('title', title);
    formData.append('company', company);
    formData.append('description', description);

    try {
      const response = await fetch('http://localhost:8000/job-listings/', {
        method: 'POST',
        body: formData
      });

      if (response.ok) {
        alertMessage = '채용 공고가 성공적으로 작성되었습니다.';
        // Clear form fields
        title = '';
        company = '';
        description = '';

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
  <h1>채용 공고 작성</h1>
  <br><br>
  {#if alertMessage}
    <div class="alert">{alertMessage}</div>
  {/if}
  <br><br>
  <form on:submit|preventDefault={handleJobPosting}>
    <label>직책:</label>
    <input type="text" bind:value={title} required />

    <label>회사:</label>
    <input type="text" bind:value={company} required />

    <label>설명:</label>
    <textarea bind:value={description} required></textarea>
  
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
  
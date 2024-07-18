<script>
  import { navigate } from 'svelte-routing';
  import Navbar from '../../components/Navbar.svelte';
  import '@fortawesome/fontawesome-free/css/all.css';

  let title = '';
  let company = '';
  let description = '';
  let audioBlob = null;
  let alertMessage = '';
  let mediaRecorder;
  let isRecording = false;
  let recordedChunks = [];

  async function handleJobPosting() {
    const formData = new FormData();
    formData.append('title', title);
    formData.append('company', company);
    formData.append('description', description);
    if (audioBlob) {
      formData.append('audio', audioBlob, 'audio.webm');
    }

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
        audioBlob = null;
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

  async function startRecording() {
    try {
      recordedChunks = [];
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorder = new MediaRecorder(stream);

      mediaRecorder.ondataavailable = event => {
        if (event.data.size > 0) {
          recordedChunks.push(event.data);
        }
      };

      mediaRecorder.onstop = () => {
        audioBlob = new Blob(recordedChunks, { type: 'audio/webm' });
        console.log("Recording stopped, audioBlob created", audioBlob);
      };

      mediaRecorder.start();
      isRecording = true;
      console.log("Recording started");
    } catch (err) {
      console.error("Error accessing media devices.", err);
      alertMessage = '오디오 장치를 사용할 수 없습니다. 권한을 확인하세요.';
    }
  }

  function stopRecording() {
    mediaRecorder.stop();
    isRecording = false;
    console.log("Recording stopped");
  }

  function toggleRecording() {
    if (isRecording) {
      stopRecording();
    } else {
      startRecording();
    }
  }
</script>

<Navbar />

<main class="container">
  <h1>채용 공고 작성</h1>
  <h4>(녹음이나 직접 작성 해주세요.)</h4>
  <br><br>
  <h2>전체 녹음</h2>
  <div>
    <button type="button" on:click={toggleRecording} class="record-button">
      <i class="fas fa-microphone"></i> {#if isRecording}녹음 중...{:else}녹음{/if}
    </button>
  </div>
  {#if alertMessage}
    <div class="alert">{alertMessage}</div>
  {/if}
  <br><br>
  <form on:submit|preventDefault={handleJobPosting}>
    <label>직책:</label>
    <div>
      <button type="button" on:click={toggleRecording} class="record-button">
        <i class="fas fa-microphone"></i> {#if isRecording}녹음 중...{:else}녹음{/if}
      </button>
    </div>
    <input type="text" bind:value={title} required />

    <label>회사:</label>
    <div>
      <button type="button" on:click={toggleRecording} class="record-button">
        <i class="fas fa-microphone"></i> {#if isRecording}녹음 중...{:else}녹음{/if}
      </button>
    </div>
    <input type="text" bind:value={company} required />

    <label>설명:</label>
    <div>
      <button type="button" on:click={toggleRecording} class="record-button">
        <i class="fas fa-microphone"></i> {#if isRecording}녹음 중...{:else}녹음{/if}
      </button>
    </div>
    <textarea bind:value={description} required></textarea>
  
    <button type="submit">작성</button>
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
</style>
  
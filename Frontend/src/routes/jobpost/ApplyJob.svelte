<script>
  import { onMount } from 'svelte';
  import { navigate, Link } from 'svelte-routing';
  import Navbar from '../../components/Navbar.svelte';
  import '@fortawesome/fontawesome-free/css/all.css';

  function getIdFromPath() {
    const path = window.location.pathname;
    const segments = path.split('/');
    return segments[segments.length - 1];
  }
  let id = null;
  let job = null;
  let error = null;

  // 해당 공고 정보 받아오기
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
      console.log('apply Job ID:', id);
      if (!job) {
        fetchJobDetail(id);
      }
    } catch (err) {
      error = err.message;
    }
  });

  let title = '';
  let company = '';
  let description = '';
  let alertMessage = '';


  // 직접 작성 제출
  async function handleJobApplying() {
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


  let mediaRecorder;
  let audioBlob = null;

  // ===================전체 녹음=======================
  let totalaudioBlob = null;
  let isTotalRecording = false;

  // 전체 녹음하기 -> audioBlob 생성
  async function totalRecording() {
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
      isTotalRecording = true;
      console.log("Recording started");
    } catch (err) {
      console.error("Error accessing media devices.", err);
      alertMessage = '오디오 장치를 사용할 수 없습니다. 권한을 확인하세요.';
    }
  }

  function stopTotalRecording() {
    mediaRecorder.stop();
    isTotalRecording = false;
    console.log("Recording stopped");
  }

  function toggleTotalRecording() {
    if (isTotalRecording) {
      stopTotalRecording();
    } else {
      totalRecording();
    }
  }

  // 녹음 파일 전송
  async function uploadTotalRecording() {
    if (audioBlob) {
      const formData = new FormData();
      formData.append(job.id, 'user', audioBlob, 'recording.webm');

      try {
        const response = await fetch('http://localhost:8000/upload', {
          method: 'POST',
          body: formData,
        });

        if (response.ok) {
          alert('파일 업로드 성공');
        } else {
          throw new Error('파일 업로드 실패');
        }
      } catch (err) {
        console.error('Error uploading file:', err);
        alert('파일 업로드 중 오류가 발생했습니다.');
      }
    } else {
      alert('녹음된 오디오가 없습니다.');
    }
    navigate('/home');
  }


  //================ 한 질문에 대해 녹음
  // let recordings = []
  // let isRecording = false;
  // async function startRecording() {
  //   try {
  //     recordedChunks = [];
  //     const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  //     mediaRecorder = new MediaRecorder(stream);

  //     mediaRecorder.ondataavailable = event => {
  //       if (event.data.size > 0) {
  //         recordedChunks.push(event.data);
  //       }
  //     };

  //     mediaRecorder.onstop = () => {
  //       const audioBlob = new Blob(recordedChunks, { type: 'audio/webm' });
  //       recordings.push(audioBlob);
  //       console.log("Recording stopped, audioBlob created", audioBlob);
  //     };

  //     mediaRecorder.start();
  //     isRecording = true;
  //     console.log("Recording started");
  //   } catch (err) {
  //     console.error("Error accessing media devices.", err);
  //     alertMessage = '오디오 장치를 사용할 수 없습니다. 권한을 확인하세요.';
  //   }
  // }

  // function stopRecording() {
  //   mediaRecorder.stop();
  //   isRecording = false;
  //   console.log("Recording stopped");
  // }

  // function toggleRecording() {
  //   if (isRecording) {
  //     stopRecording();
  //   } else {
  //     startRecording();
  //   }
  // }

  // function playRecording(index) {
  //   if (recordings[index]) {
  //     const audioUrl = URL.createObjectURL(recordings[index]);
  //     const audio = new Audio(audioUrl);
  //     audio.play();
  //   } else {
  //     alert('녹음된 오디오가 없습니다.');
  //   }
  // }

  // async function uploadRecordings() {
  //   if (recordings.length > 0) {
  //     const formData = new FormData();
  //     recordings.forEach((recording, index) => {
  //       formData.append('files[]', recording, `recording${index + 1}.webm`);
  //     });

  //     try {
  //       const response = await fetch('http://localhost:8000/upload', {
  //         method: 'POST',
  //         body: formData,
  //       });

  //       if (response.ok) {
  //         alert('파일 업로드 성공');
  //       } else {
  //         throw new Error('파일 업로드 실패');
  //       }
  //     } catch (err) {
  //       console.error('Error uploading files:', err);
  //       alert('파일 업로드 중 오류가 발생했습니다.');
  //     }
  //   } else {
  //     alert('녹음된 오디오가 없습니다.');
  //   }
  // }
</script>

<Navbar />

<main class="container">
  <h1>{job?.company}의 이력서 작성</h1>
  <h4>(녹음 또는 직접 작성 해주세요.)</h4>
  <br><br>
  <h3>전체 녹음</h3>
  <div>
    <button type="button" on:click={toggleTotalRecording} class="record-button">
      <i class="fas fa-microphone"></i> {#if isTotalRecording}녹음 중...{:else}녹음{/if}
    </button>
    <button type="button" on:click={uploadTotalRecording} class="upload-button">
      <i class="fas fa-upload"></i> 녹음 파일로 제출
    </button>
  </div>
  
  {#if alertMessage}
    <div class="alert">{alertMessage}</div>
  {/if}
  <br><br>
  
  <form on:submit|preventDefault={handleJobApplying}>
    <label>이름</label>
    <input type="text" bind:value={title} required placeholder={job?.company} />

    <!-- <label>경력 사항
      <button type="button" on:click={toggleRecording} class="record-button">
        <i class="fas fa-microphone"></i> {#if isRecording}녹음 중...{:else}녹음{/if}
      </button>
    </label>
    <input type="text" bind:value={company} required placeholder={job?.title} />

    <label>설명
      <button type="button" on:click={toggleRecording} class="record-button">
        <i class="fas fa-microphone"></i> {#if isRecording}녹음 중...{:else}녹음{/if}
      </button>
    </label>

    <textarea bind:value={description} required placeholder="글 설명"></textarea> -->
  
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
  
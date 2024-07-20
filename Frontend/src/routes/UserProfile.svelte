<script>
  import { navigate } from 'svelte-routing';
  import Navbar from '../components/Navbar.svelte';
  import { user, userType } from '../lib/store';


  let currentUser; // 필요시 실제 유저 ID로 설정
  let currentUserType;
  let name = '';
  let birth = '';
  let gender = '';
  let skills = [];
  let careers = [];
  let alertMessage = '';

  user.subscribe(value => {
    currentUser = value;
  });

  userType.subscribe(value => {
    currentUserType = value;
  });

  // 기술 리스트에 추가 및 삭제
  function addSkill() {
      skills = [...skills, ''];
  }
  function removeSkill(index) {
      skills = skills.filter((_, i) => i !== index);
  }
  
  // 경력 리스트에 추가 및 삭제
  function addCareer() {
      careers = [...careers, { startDate: '', endDate: '', affiliation: '', summary: '' }];
  }

  function removeCareer(index) {
      careers = careers.filter((_, i) => i !== index);
  }

  async function handleProfileSubmission(event) {
      event.preventDefault();
      const timestamp = new Date().toISOString();

      const profileData = {
          username: currentUser,
          name: name,
          birth: birth,
          gender: parseInt(gender, 10),
          skills: skills,
          careers: careers,
          createdAt: timestamp,
          updatedAt: timestamp
      };
      
      try {
          const response = await fetch('http://localhost:8000/profile/save', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json'
              },
              body: JSON.stringify(profileData)
          });

          console.log(profileData);

          if (response.ok) {
            console.log('success');

            alertMessage = '프로필이 성공적으로 작성되었습니다.';
            // Clear form fields
            name = '';
            birth = '';
            gender = '';
            skills = [];
            careers = [];

            setTimeout(() => {
                alertMessage = '';
                navigate('/home');
            }, 2000); // 2초 후에 홈 페이지로 이동
          } else {
              const result = await response.json();
              alertMessage = `작성 실패: ${result.detail}`;
          }
      } catch (error) {
          alertMessage = `작성 실패: 서버 오류 - ${error.message}`;
      }
  }

  function handleRadioChange(event) {
    gender = event.target.value;
    console.log("Selected gender:", gender);
  }

</script>

<Navbar />
<main class="container">
    <h1>나만의 프로필 작성</h1>
    {#if alertMessage}
        <div class="alert">{alertMessage}</div>
    {/if}
    <form on:submit|preventDefault={handleProfileSubmission}>
      <label>
          이름
          <input type="text" bind:value={name} required />
        </label>
        <label>
          생년월일:
          <input type="date" bind:value={birth} required />
        </label>

        <div class="radio-group">
          <label>남자<input type="radio" name="gender" value=1 on:change={handleRadioChange} />
          </label>
          <label>여자<input type="radio" name="gender" value=2 on:change={handleRadioChange} />
          </label>
        </div>

        <fieldset>
          <legend>기술</legend>
          {#each skills as skill, index}
            <label> 보유 기술 {index + 1}:</label>
              <br>
              <div>
                  <input type="text" bind:value={skills[index]} placeholder="프로그래밍" required />
                  <button type="button" on:click={() => removeSkill(index)}>기술 삭제</button>
              </div>
          {/each}
          <br>
          <button type="button" on:click={addSkill}>기술 추가하기</button>
        </fieldset>
        <br><br>
        <fieldset>
          <legend>경력 사항</legend>
          {#each careers as career, index}
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

                <button type="button" on:click={() => removeCareer(index)}>경력 삭제</button>
            </div>
          {/each}
          <br>
          <button type="button" on:click={addCareer}>경력 추가</button>
        </fieldset>
        <br><br>
      <button type="submit">작성</button>
    </form>
</main>

<style>
  legend{
    font-weight: bold;
    font-size: 1.2em; /* 글자 크기 조절 */
    color:green;
  }
  main {
    font-family: Arial, sans-serif;
    padding: 20px;

  }
  .radio-group {
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
    align-items: center;
    margin-left: 320px;
  }
  
  input[type="radio"] {
    margin-right: 5px;
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
  
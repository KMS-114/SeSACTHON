<script>
  import { navigate } from 'svelte-routing';
</script>

<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body, html {
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f8f9fa;
  }
  .logotxt {
    color:black;
  }
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: white;
    padding: 10px 20px;
    color: black;
    position: fixed;
    width: 100%;
  }

  .navbar a {
    color: #f2f2f2;
    text-decoration: none;
    padding: 8px 16px;
  }

  .navbar a:hover {
    background-color: #ddd;
    color: black;
  }
  .navbar-link {
    margin: 0 1rem;
    text-decoration: none;
    color: black; /* 글자 색깔을 검정색으로 설정 */
  }

  .container {
    padding: 20px;
    max-width: 1200px;
    margin: auto;
    width: 100%;
    position:relative;
    top: 0px;
  }

  .search-form {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
  }

  .search-bar {
    width: 100%;
    padding: 12px;
    margin: 8px 0;
    box-sizing: border-box;
  }

  .cb-filters-wrap {
    display: flex;
    justify-content: space-between;
  }

  .cb-filters-wrap label {
    display: flex;
    align-items: center;
  }

  .cb-filters-wrap input {
    margin-right: 10px;
  }

  .job-flex_rel {
    display: flex;
    justify-content: space-between;
  }

  .wide-list {
    width: 70%;
  }

  .job-card_main {
    background: white;
    padding: 15px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
  }

  .new-card-content {
    display: flex;
    flex-direction: column;
  }

  .info-wrap {
    margin-bottom: 10px;
  }

  .right-job-box {
    width: 28%;
  }

  .big-button {
    display: block;
    width: 100%;
    text-align: center;
    background-color: #28a745;
    color: white;
    padding: 10px;
    border-radius: 5px;
    text-decoration: none;
    margin-bottom: 20px;
  }

  .big-button:hover {
    background-color: #218838;
  }

  .card-padding {
    padding: 15px;
    background-color: #f8f9fa;
    border-radius: 5px;
    border: 1px solid #ccc;
  }

  .toast-wrapper {
    position: fixed;
    bottom: 10px;
    right: 10px;
    width: 300px;
    z-index: 1000;
  }

  .toast-box-d {
    padding: 10px;
    background-color: #444;
    color: #fff;
    border-radius: 5px;
    margin-bottom: 10px;
  }

  .toast-box-d.red {
    background-color: #e40023;
  }

  .toast-content {
    display: flex;
    align-items: center;
  }

  .toast-content .toast-icon-d {
    margin-right: 10px;
  }
</style>

<div class="navbar">
  <a href="/" class="navbar_logo-link w-nav-brand w--current">
    <div class="logotxt">거대<span class="text-brand">박격포</span></div>
  </a>
  <div>
    <a class="button in-nav w-button" on:click={() => navigate('/job-post-submission-form')}>Post a job</a>
  </div>
</div>

<div class="container">
  <form id="email-form" name="email-form" action="/" method="get" class="search-form">
    <input class="search-bar" maxlength="256" name="job-search" placeholder="Search for a job..." type="text" id="job-search" />
    <div class="cb-filters-wrap">
      <label>
        <input type="checkbox" name="Remote" />
        Remote
      </label>
      <label>
        <input type="checkbox" name="In Office" />
        In Office
      </label>
    </div>
  </form>

  <div class="job-flex_rel">
    <div class="wide-list">
      <div class="job-card_main">
        <div class="new-card-content">
          <div class="info-wrap">
            <a href="/job-posts/test-d657a" class="h3_job">test</a>
            <div class="spacer-10"></div>
            <div class="flex-center space-between">
              <div class="location-wrap">
                <div class="icon-jobs w-embed">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M7 5V2C7 1.73478 7.10536 1.48043 7.29289 1.29289C7.48043 1.10536 7.73478 1 8 1H16C16.2652 1 16.5196 1.10536 16.7071 1.29289C16.8946 1.48043 17 1.73478 17 2V5H21C21.2652 5 21.5196 5.10536 21.7071 5.29289C21.8946 5.48043 22 5.73478 22 6V20C22 20.2652 21.8946 20.5196 21.7071 20.7071C21.5196 20.8946 21.2652 21 21 21H3C2.73478 21 2.48043 20.8946 2.29289 20.7071C2.10536 20.5196 2 20.2652 2 20V6C2 5.73478 2.10536 5.48043 2.29289 5.29289C2.48043 5.10536 2.73478 5 3 5H7ZM4 16V19H20V16H4ZM4 14H20V7H4V14ZM9 3V5H15V3H9ZM11 11H13V13H11V11Z" fill="currentColor" />
                  </svg>
                </div>
                <p class="paragraph">test</p>
              </div>
              <div class="location-wrap">
                <div class="icon-jobs w-embed">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M7 5V2C7 1.73478 7.10536 1.48043 7.29289 1.29289C7.48043 1.10536 7.73478 1 8 1H16C16.2652 1 16.5196 1.10536 16.7071 1.29289C16.8946 1.48043 17 1.73478 17 2V5H21C21.2652 5 21.5196 5.10536 21.7071 5.29289C21.8946 5.48043 22 5.73478 22 6V20C22 20.2652 21.8946 20.5196 21.7071 20.7071C21.5196 20.8946 21.2652 21 21 21H3C2.73478 21 2.48043 20.8946 2.29289 20.7071C2.10536 20.5196 2 20.2652 2 20V6C2 5.73478 2.10536 5.48043 2.29289 5.29289C2.48043 5.10536 2.73478 5 3 5H7ZM4 16V19H20V16H4ZM4 14H20V7H4V14ZM9 3V5H15V3H9ZM11 11H13V13H11V11Z" fill="currentColor" />
                  </svg>
                </div>
                <p class="paragraph">test</p>
              </div>
              <div class="location-wrap">
                <div class="icon-jobs w-embed">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 23.7279L5.636 17.3639C4.37734 16.1052 3.52019 14.5016 3.17293 12.7558C2.82567 11.0099 3.00391 9.20035 3.6851 7.55582C4.36629 5.91129 5.51984 4.50569 6.99988 3.51677C8.47992 2.52784 10.22 2 12 2C13.78 2 15.5201 2.52784 17.0001 3.51677C18.4802 4.50569 19.6337 5.91129 20.3149 7.55582C20.9961 9.20035 21.1743 11.0099 20.8271 12.7558C20.4798 14.5016 19.6227 16.1052 18.364 17.3639L12 23.7279ZM16.95 15.9499C17.9289 14.9709 18.5955 13.7236 18.8656 12.3658C19.1356 11.0079 18.9969 9.60052 18.4671 8.32148C17.9373 7.04244 17.04 5.94923 15.8889 5.18009C14.7378 4.41095 13.3844 4.00043 12 4.00043C10.6156 4.00043 9.26222 4.41095 8.11109 5.18009C6.95996 5.94923 6.06275 7.04244 5.53292 8.32148C5.00308 9.60052 4.86442 11.0079 5.13445 12.3658C5.40449 13.7236 6.07111 14.9709 7.05 15.9499L12 20.8999L16.95 15.9499V15.9499ZM12 12.9999C11.4696 12.9999 10.9609 12.7892 10.5858 12.4141C10.2107 12.0391 10 11.5304 10 10.9999C10 10.4695 10.2107 9.96078 10.5858 9.58571C10.9609 9.21064 11.4696 8.99992 12 8.99992C12.5304 8.99992 13.0391 9.21064 13.4142 9.58571C13.7893 9.96078 14 10.4695 14 10.9999C14 11.5304 13.7893 12.0391 13.4142 12.4141C13.0391 12.7892 12.5304 12.9999 12 12.9999Z" fill="currentColor" />
                  </svg>
                </div>
                <p class="paragraph">New york</p>
              </div>
            </div>
          </div>
          <div class="date-light">1 Feb</div>
        </div>
      </div>
    </div>
    <div class="right-job-box">
      <a href="/job-post-submission-form" class="big-button w-button" on:click={() => navigate('/job-post-submission-form')}>Post a job<br /><span class="small-in-button">100% free!</span></a>
      <div class="card-padding">
        <p><strong>Discover qualified candidates to fill your open positions on CrunchBoard.<br /><br />‍</strong>CrunchBoard is the official job board of TechCrunch, leveraging an engaged and specialized audience each month to help you get your job vacancies filled. Jobs posted on CrunchBoard will be visible on the TechCrunch network including the website, daily newsletters and social channels.</p>
      </div>
    </div>
  </div>
</div>

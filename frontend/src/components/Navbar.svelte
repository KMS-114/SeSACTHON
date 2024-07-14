<script>
    import { navigate } from 'svelte-routing';
</script>

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a class="nav-link" href="/">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" on:click="{() => navigate('/jobpostlist')}">Job Posting</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/login">Profile</a>
                </li>
            </ul>
            <div class="text-end">
                <button type="button" class="btn btn-outline-light me-2" on:click={() => navigate('/jobpost')}>jobpost</button>
                <button type="button" class="btn btn-outline-light me-2" on:click={() => navigate('/login')}>Login</button>
                <button type="button" class="btn btn-warning" on:click={() => navigate('/signup')}>Signup</button>
            </div>
        </div>
    </div>
</nav>

<style>
    .navbar {
        margin-bottom: 20px; /* 간격을 줄임 */
        position: fixed;
        width: 100%;
    }

    .navbar-nav {
        display: flex;
        justify-content: space-between;
        width: 100%;
        padding-left: 0;
        margin: 0 0px; /* 간격을 더 작게 조정 */
    }

    .navbar-nav .nav-link {
        padding: 10px 15px; /* 링크의 패딩 조정 */
        font-family: Arial, sans-serif; /* 폰트 변경 */
        font-size: 20px; /* 폰트 크기 변경 */

    }
    .text-end {
        display: flex;
        align-items: center;
    }
</style>

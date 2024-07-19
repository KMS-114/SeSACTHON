<script>
    import { Router, Route, navigate, Link } from 'svelte-routing';
    import Main from './routes/Main.svelte';
    import Home from './routes/Home.svelte';
    import Login from './routes/Login.svelte';
    import Signup from './routes/Signup.svelte';
    import JobPostList from './routes/jobpost/JobPostList.svelte';
    import JobPost from './routes/jobpost/JobPost.svelte';
    import JobDetail from './routes/jobpost/JobDetail.svelte';
    import UserProfile from './routes/UserProfile.svelte';
    import ApplyJob from './routes/jobpost/ApplyJob.svelte';
    import MyJobPostList from'./routes/jobpost/MyJobPostList.svelte'
    import { isLoggedIn, userType } from './lib/store';


    // 처음 접속 시 메인 페이지로 리디렉션
    if (!localStorage.getItem('token')) {
        navigate('/', { replace: true });
    }

    let loggedIn = true;
    let currentUserType = "2";

    // 로그인 상태 구독
    isLoggedIn.subscribe(value => {
        loggedIn = value;
    });

    // 고용주, 지원자 상태
    userType.subscribe(value => {
        currentUserType = value;
    });

    // 라우터 가드 기능
    function requireAuth(path, component) {
    return {
        path,
        component,
        action: () => {
        if (!loggedIn) {
            navigate('/login'); // 로그인되지 않은 경우 로그인 페이지로 리디렉션
            }
        }
    };
    }
</script>

<Router>
    <Route path="/" component={Main} />
    <Route path="/login" component={Login} />
    <Route path="/signup" component={Signup} />
    {#if loggedIn}
        <Route path="/home" component={Home} />
        <Route path="/jobpostlist" component={JobPostList} />
        <Route path="/jobdetail/:id" component={JobDetail} />

        <Route path="/myjobpostlist" component={MyJobPostList} />
        <!-- {#if currentUserType === "1"} -->
            <Route path="/jobpost" component={JobPost} />
        <!-- {/if} -->
        <!-- {#if currentUserType === "2"} -->
            <Route path="/profile" component={UserProfile} />
        <!-- {/if} -->
        <Route path="/applyjob/:id" component={ApplyJob} />
    {/if}

</Router>
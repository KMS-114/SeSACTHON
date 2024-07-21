<script>
    import { Router, Route, navigate, Link } from 'svelte-routing';
    import Main from './routes/Main.svelte';
    import Home from './routes/Home.svelte';

    import Login from './routes/user/Login.svelte';
    import Signup from './routes/user/Signup.svelte';
    import myInfo from './routes/user/myInfo.svelte';

    import JobPostList from './routes/jobpost/JobPostList.svelte';
    import JobPost from './routes/jobpost/JobPost.svelte';
    import JobDetail from './routes/jobpost/JobDetail.svelte';
    import ApplyUserList from'./routes/jobpost/ApplyUserList.svelte';
    import MyJobPostList from'./routes/jobpost/MyJobPostList.svelte'

    import MyResume from'./routes/applicant/MyResume.svelte'
    import ApplyJob from './routes/applicant/ApplyJob.svelte';

    import UserProfile from './routes/UserProfile.svelte';

    import { isLoggedIn, userType } from './lib/store';


    // 처음 접속 시 메인 페이지로 리디렉션
    if (!localStorage.getItem('token')) {
        navigate('/', { replace: true });
    }

    let loggedIn = true;
    let currentUserType;

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
    <Route path="/myInfo" component={myInfo} />

    {#if loggedIn}
        <Route path="/home" component={Home} />

        <Route path="/jobpostlist" component={JobPostList} />
        <Route path="/jobdetail/:id" component={JobDetail} />
        <Route path="/myjobpostlist" component={MyJobPostList} />
        <Route path="/jobpost" component={JobPost} />
        <Route path="/applyuserlist/:id" component={ApplyUserList} />

        
        <Route path="/profile" component={UserProfile} />
        <Route path="/applyjob/:id" component={ApplyJob} />
        <Route path="/myresume" component={MyResume} />
    {/if}

</Router>
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

    // 처음 접속 시 메인 페이지로 리디렉션
    if (!localStorage.getItem('token')) {
        navigate('/', { replace: true });
    }
</script>

<Router>
    <Route path="/" component={Main} />
    <Route path="/home" component={Home} />
    <Route path="/login" component={Login} />
    <Route path="/signup" component={Signup} />
    <Route path="/jobpostlist" component={JobPostList} />
    <Route path="/jobpost" component={JobPost} />
    <Route path="/jobdetail:id" component={JobDetail} />
    <Route path="/profile" component={UserProfile} />
</Router>
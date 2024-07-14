<script>
    import { Router, Route, navigate } from 'svelte-routing';
    import Home from './routes/Home.svelte';
    import Login from './routes/Login.svelte';
    import Signup from './routes/Signup.svelte';
    import JobPost from './routes/JobPost.svelte';

    // 처음 접속 시 로그인 페이지로 리디렉션
    if (!localStorage.getItem('token')) {
        navigate('/', { replace: true });
    }
</script>

<Router>
    <Route path="/" component={Home} />
    <Route path="/login" component={Login} />
    <Route path="/signup" component={Signup} />
    <Route path="/jobpost" component={JobPost} />
</Router>
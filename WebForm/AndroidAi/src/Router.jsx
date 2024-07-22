import { createBrowserRouter } from 'react-router-dom';
import App from './App.jsx';
import Login from './Pages/Login.jsx';
import NotFound from './components/NotFound.jsx';
import SignUP from './Pages/SignUp.jsx'

const Router = createBrowserRouter([
    {
        path: '/',
        element: <App />,
        errorElement: <NotFound />,
        children: [
          {
            path: 'login',
            element: <Login />,
          },
          {
            path:'signup',
            element:<SignUP></SignUP>
          }
        ],
      },
]);

export default Router;

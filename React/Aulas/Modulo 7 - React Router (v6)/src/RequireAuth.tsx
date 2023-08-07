import { Navigate } from 'react-router-dom'
import { Home } from './pages/Home'

type Props = {
    children: JSX.Element
}

export const RequireAuth = ({children}:Props) => {
    const isAuth = true

    if(!isAuth) {
        
        return <Home/> //Renderia a página, caso não aconteça a requisição
    }
    return children
}
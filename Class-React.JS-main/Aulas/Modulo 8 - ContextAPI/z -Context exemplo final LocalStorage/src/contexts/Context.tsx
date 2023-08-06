import { createContext, useReducer } from "react";
import { useEffect } from "react";
import { reducerActionType } from "../types/reducerActionsType";

//Imports
import {UserType, userInitialState, userReducer } from '../reducers/userReducer'
import { themeReducer, themeInitialState, ThemeType  } from "../reducers/themeReducer";


//Campo editável
type initialStateType = {
    user: UserType;
    theme: ThemeType
}

type ContextType = {
    state: initialStateType
    dispatch: React.Dispatch<any>
}

///Campo editável
const initialState = {
    user: userInitialState,
    theme: themeInitialState
}



export const Context = createContext<ContextType>({
    state: initialState,
    dispatch: () => null
})

///Campo editável
const mainReducer = (state: initialStateType, action: reducerActionType) => ({
    user: userReducer(state.user, action),
    theme: themeReducer(state.theme, action)
})

export const ContextProvider: React.FC<{children: React.ReactNode}> = ({children}) => {
    
    const [state, dispatch] = useReducer(mainReducer, initialState)

    //coloque dentro do useEffect as função que queira guardar no localStorage
    useEffect(() => {
        localStorage.setItem('theme', state.theme.status as string)
    })

    return (
        <Context.Provider value={{state, dispatch}} >
            {children}
        </Context.Provider>
    )

}
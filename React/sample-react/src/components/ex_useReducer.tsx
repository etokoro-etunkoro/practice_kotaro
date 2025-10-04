import { useReducer } from "react";
//reducerが受け取るactionの型を定義
type Action = 'DECREMENT' | 'INCREMENT' | 'SQUARED'| 'RESET';
//現状とactionを受け取り、新しい状態を返す関数
const reducer = (currentCount: number, action: Action) => {
    switch(action){
        case 'INCREMENT':
            return currentCount + 1;
        case 'DECREMENT':
            return currentCount - 1;
        case 'SQUARED':
            return currentCount ** 2;
        case 'RESET':
            return 1;
        default:
            return currentCount;
    }
}
type CounterProps = {
    initialValue: number
}
const Counter = (props: CounterProps) => {
    const {initialValue} = props
    const [count, dispatch] = useReducer(reducer, initialValue);
    return(
        <div>
            <p>Count: {count}</p>
            <button onClick={() => dispatch('INCREMENT')}>Increment</button>
            <button onClick={() => dispatch('DECREMENT')}>Decrement</button>
            <button onClick={() => dispatch('SQUARED')}>squared</button>
            <button onClick={() => dispatch('RESET')}>reset</button>
        </div>
    )
}

export default Counter
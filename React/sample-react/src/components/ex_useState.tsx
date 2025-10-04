import { useState } from "react"
type CounterProps = {
  initialValue?: number
}

const Counter = (props: CounterProps) => {
    const {initialValue} = props
    // カウントを保持する状態をuseState()で宣言
    // 引数には初期値を設定
    // count: 現在の状態, setCount: 状態を更新する関数
    const [count, setCount] = useState(initialValue)
    // const[状態, 状態を更新する関数] = useState(初期値)

    return(
        <div>
            <p>Count: {count}</p>
            {/* ボタンがクリックされたときにsetCountを呼び出し、countの値を1増やす */}
            <button onClick={() => setCount((count ?? 0) + 1)}>Increment</button>
            <button onClick={() => setCount((count ?? 0) - 1)}>Decrement</button>
            <button onClick={() => setCount((count ?? 0) ** 2)}>squared</button>
        </div>
    )
}
export default Counter
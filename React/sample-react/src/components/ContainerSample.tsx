import React from "react";
type ContainerProps = {
    title: string
    children: React.ReactNode
}
const Container = (props: ContainerProps) : React.JSX.Element => {
    const { title, children } = props;
    return (
        <div style={{border: 'solid 2px black', padding: '8px', margin: '8px', backgroundColor: 'lightblue'}}>
            <span>{title}</span>
            {/* childrenは、Containerコンポーネントの開始タグと終了タグの間に挟まれた要素を表す */}
        </div>
    )
}  
const Patent = (): React.JSX.Element => {
    return (
        <Container title="これはContainerコンポーネントです">
            <div>ここの部分が背景色で囲まれます</div>
        </Container>
    )
}
export default Patent;
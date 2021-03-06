개념 및 분류

### 순차 자료구조와 선형 리스트

배열

리스트

연결리스트

Array vs LinkedList

Dynamic Arrau

Dynamic Array vs LinkedList

### Stack

Queue

2개의 스택으로 큐 구현하기

### Tree

BST

Heap

Heapify

B Tree & B+ Tree

Trie

RedBlackTree

### Graph

### Hash

## 개념 및 분류

**자료구조의 개념**

자료를 효율적으로 표현하고 저장하고 처리할 수 있도록 하는 것

학습 이유: 컴퓨터가 효율적으로 문제를 처리하기 위해 필요한 개념이라서

**자료의 형태에 따른 분류**

단순 구조

- 정수, 실수, 문자, 문자열 등 기본 자료형

선형 구조

- 자료들 사이의 관계가 1:1
- 순차 리스트, 연결 리스트(단순, 이중, 원령), 스택, 큐, 데크 등

비선형 구조

- 자료들 사이의 관계가 1:다, 또는 다:다 관계
- 트리(일반, 이진), 그래프(방향, 무반향)

파일 구조

- 서로 관련 있는 필드로 구성된 레코드의 집합인 파일에 대한 구조
- 순차 파일, 색인 파일, 직접 파일 등

## 순차 자료구조와 선형 리스트

**순차 자료구조**

구현할 자료들을 논리적 순서로 메모리에 연속 저장하는 구현 방식, 논리적 순서, 문리적 순서 일치

삽입, 삭제 연산을 해도 빈자리 없이 연속해 저장, 변경된 논리적 순서와 저장된 물리적 순서가 일치

**순차 자료구조의 문제점**

삽입 연산이나 삭제 연산 후 연속적인 물리 주소를 유지하기 위해 원소들을 이동 시키는 추가 작업과 시간이 소요됨, 이러한 이동작업으로 인해 오버헤드등의 문제가 발생 

배열을 이용해 구현하기 때문에 배열이 갖고 있는 메모리 사용의 비효율성 문제를 그대로 가짐

**연결 자료 구조**

물리적 위치, 물리적 순서와 상관 없이 링크에 의해 논리적인 순서를 표현하는 구현 방식

→물리적인 순서를 맞추기 위한 오버헤드가 발생하지 않음

→ 여러 개의 작은 공간을 연결해 하나의 자료구조를 표현하기 때문에 크기 변경이 유연하고 더 효율적으로 메모리를 사용한다.

삽입, 삭제 연산을 해 논리적 순서가 변경되어도, 링크 정보만 변경되고 물리적 순서는 변경 안됨

## 배열(Array)

- 메모리 상에 인접하게 데이터가 존재하는 형태의 자료구조(연속적으로 이루어짐)
- 논리적 저장 순서와 물리적 저장 순서가 일치
- Random Access 가능 - 인덱스로 원소에 접근 가능, 인덱스를 알고 있을 시 O(1)의 시간 복잡도로 접근 가능
- 삭제, 삽입 시 원소에 접근에 해당 작업 완료 후 shift를 해줘야 해 O(n)의 시간복잡도를 가진다.
- 메모리 공간 활요에 제약 있음
- 

## 연결 리스트(Linked List)

- 메모리 주소 값을 활용하여 다음 원소의 위치를 가리키게 해 다음 데이터와의 연결을 만드는 형태의 자료구조, 리스트의 연결 자료구조로 표현
- 연결 방식에 따라, 원형 연결 리스트, 이중 연결 리스트, 이중 원형 연결 리스트
- 논리적 저장 순서와 물리적 저장 순서가 일치하지 않아 탐색시 처음 노드부터 순회해야 함. O(n)
- 사용자는 첫 번째 노드의 위치만 알고 있다.
- 삽입, 삭제 시 그 원소를 찾는 시간 O(n), 작업 시간 O(1)이 걸려 모든 작업 완료까지 O(n)의 시간이 걸린다.

* *리스트: 자료를 구조화 하는 가장 기본적인 방법은 나열하는 것

**연결 리스트의 노드** 

하나의 원소를 표현하기 위한 단위 구조, <원소(값을 정장하는 데이터 필드), 주소(링크 필드)>

**원형 연결 리스트** 

단순 연결 리스트에서 마지막 노드가 리스트의 첫 번째 노드를 가리키게 해 리스트 구조를 원형으로 만든 연결 리스트

**이중 연결 리스트**

리스트를 양쪽 방향으로 순회할 수 있도록 링크 필드를 두 개 사용해 양반향 노드으로 노드를 연결한 히스트

## Array vs Linked List

데이터 접근 속도

Array: O(1)-인덱스를 사용해

LinkedList: O(n)-처음부터 순차적 검색

데이터 삽입 속도

Array:  O(n) - shift, 중간이나 맨앞에 삽입 시 이후의 데이터를 Shift해야해서 추가 과정과 시간이 소요 따라서, 데이터가 많은 경우 비효율적

LinkedList: O(n) - 맨 앞, 맨 뒤 삽입시 O(1) 그 외, 위치 찾기 O(n) + 삽입 연산 O(1) 그럼에도 불구하고 **Array 보다 빠르다.**

Array의 경우 모든 공간이 차게 되면 새로운 메모리 공간을 할당 받아야 하나 LinkedList는 추가할때마다 동적으로 할당 받는다.

데이터 삭제 속도

Array: O(n)

LinkedList: O(n), **Array 보다 빠르게** 연산 수행

## Dynamic Array  (JAVA - ArrayList, C++ - Vector)

- 크기가 고정되지 않은 배열
- 인덱스를 가지고 있어 데이터 검색에 적합하고 속도가 빠르다.
    - 시간 복잡도 : O(1)
- 데이터의 삽입, 삭제 시 해당 데이터를 제외한 모든 데이터를 임시 배열을 생성해 **복사**하므로 삽입, 삭제가 빈번할 경우 속도가 느리며 부적합하다.
    - 시간 복잡도 : O(n)

**Java ArrayList의 경우동기화를 지원하지 않아 Vector보다 빠르다.

**동적 할당 배열과는 다름 동적 할당 배열은 배열이 할당됭 때 크기가 고정

## Dynamic Array vs LinkedList

데이터의 검색이 주가 되는 경우 Dynamic Array(ArrayList)를

데이터의 삽입, 삭제가 빈번하다면 LinkedList(삽입 삭제시 복사 과정이 없음)를 사용하는 편이 낫다.

## Stack

- 구조와 크기가 같은 자료를 정해진 방향으로 만 쌓을 수 있고, top으로 정한 한 곳을 통해서만 접근할 수 있도록 제한한 자료구조
- push - 삽입, pop-삭제
- 후입선출LIFO(Last in First Out), 나중에 들어간 원소가 먼저 나오는 구조이다.
- 시간 복잡도 : O(n)
- 공간 복잡도 : O(n)
- 응용: 삽입 순서, 삭제 순서의 역순 또는 요청 순서와 처리순서의 연순관계를 관리 할 수 있다.

→안드로이드의 액티비티를 관리하는 데 스택이 사용된다.

→ 함수의 콜 스택, 문자열 역순 출력, 연산자 후위 표기법 등

## Queue

- 리스트의 한 쪽 끝에서는 삽입 작업이, 반대쪽 끝에서는 삭제 작업이 이뤄져서 삽입된 순서대로 삭제되는 유한 순서 리스트
- FIFO(First in First out)의 구조.
- 시간 복잡도 : O(n)
- 공간 복잡도 : O(n)
- 큐의 응용:  선입선출 방식으로 처리해야 하는 문제

→안드로이드의 경우, 루퍼의 메시지 큐가 예시 중 하나이다.

→작업 버퍼 큐, 프로세스 스케쥴링, 대기행렬을 모델링하는 시뮬레이션 등

** **데크** 

큐의 양쪽 끝에서 삽입과 삭제가 모두 가능하도록 큐를 확장한 자료구조

스택의 성질, 큐의 성질을 모두 가짐

## 2개의 스택으로 큐 구현하기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/faa87c10-c649-4e72-910a-5461991bc9b2/Untitled.png)

1. inbox에 데이터를 삽입한다(push) -> A,B
2. inbox에 있는 데이터를 추출(pop)하여 outbox에 삽입(push) 한다. -> B,A
3. outbox에 있는 데이터를 추출(pop)한다. -> A,B 순으로 출력된다.

<aside>
🖍️ import java.util.Stack; //import

public class StackExample {

public static void main(String[] args){

//Stack<Integer> stack = new Stack<>(); //int형 스택 선언
Stack<String> inbox= new Stack<>(); //char형 스택 선언

Stack<String> outbox = new Stack<>();

inbox.push("A");     // stack에 값 A 추가
inbox.push("B");     // stack에 값 B 추가

outbox.push(inbox.pop());

outbox.push(inbox.pop());

}

}

</aside>

## Tree

- 원소들 간에 1: n 관계를 가지는 비선형 자료구조 중 원소 간 계층 관계를 가진 계층형 자료구조이다.
- 상위 원소에서 하위 원소로 내려가면서 확장되는 트리모양의 구조
- 루트 노드를 제외한 모든 노드는 단 하나의 부모 노드만을 갖는다.

**구성요소**

- Node : 트리를 구성하는 각각의 요소.
- Edge : 트리를 구성하기 위해 노드와 노드를 연결하는 선.
- Root Node : 트리 구조에서 최상위에 있는 노드.
- Terminal Node : 하위에 다른 노드가 연결되어 있지 않은 노드.
- Internal Node : 단말 노드를 제외한 모든 노드로 루트 노드를 포함한다
- 형제노드, 조상노드등
- 서브트리: 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리

**차수(degree)**

- 노드의 차수 : 노드에 연결된 자식 노드의 수
- 트리의 차수 : 트리에 있는 노드의 차수 중 가장 큰 값
- 단말 노드(리프노드): 차수가 0인 노드, 자식 노드가 없는 노드

**높이**

노드의 높이: 루트에서 노드에 이르는 간선의 수, 노드의 레벨

트리의 높이: 트리에 있는 노드의 높이 중 가장 큰 값, 최대 레벨

**포리스트**: 서브트리의 집합

## 이진트리

- 모든 노드의 차수를 2이하로 정해 트리의 전체 차수가 2이하가 되도록 만든 트리
- 이진 트리의 모든 노드는 왼쪽 자식 노드와 오른쪽 자식 노드만 가진다.
- 노드가 N개인 이진트리는 항상 간선이 (n-1)개이다
- 높이가 H인 이진 트리가 가질 수 있는 노드 개수는 최소 (H+1), 최대 (2^(H+1)-1)개 이다

### 이진 트리의 순회

이진 트리에 있는 모든 노드를 한 번씩 **모두 방문해** 노드가 가지고 있는 데이터를 처리하는것을 의미

(모든 원소를 빠트리거나 중복 없이 처리)

**순회방법:** 전위순회(현→왼→오), 중위 순회(왼→현→오), 후위 순회(왼→오→현)

### 이진 트리의 종류

포화 이진 트리, 완전 이진 트리, 편향 이진 트리, 불완전한 이진 트리

### - 포화 이진 트리

- 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
- 레벨 별로 노드의 개수가 1,2,4,8,16 ... 으로 늘어난다. 따라서 일반적인 이진트리에서 각 레벨 별 최대 노드의 개수는 2^(k - 1)이 된다.
- 높이가 h일 때, 최대의 노드 개수인 (2^(h+1)-1)의 노드를 가진 이진 트리 (레벨 별 노드는 공비가 2인 등비수열이라고 볼 수 있으므로)
- 루트를 1번으로 하여 2h+1-1까지 정해진 위치에 대한 노드 번호를 가짐

### - 완전 이진 트리

- 왼쪽에서 오른쪽으로 순서대로 채워진 이진트리
- 높이가 h이고 노드 수가 n개일 때 (단, n < 2h+1-1 ), 노드 위치가 포화 이진
트리에서의 노드 1번부터 n번까지의 위치와 완전히 일치하는 이진 트리
- 완전 이진 트리에서는 (n+1)번부터 (2h+1-1 )번까지 노드는 모두 공백 노드

### - 편향 이진 트리

높이가 h일 때 h+1개의 노드를 가지면서 모든 노드가 왼쪽이나 오른쪽 중 한 방향으로만 서브 트리를 가지고 있는 트리

### - 이진 탐색 트리

이진 트리를 탐색용 자료구조로 사용하기 위해 원소 크기에 따라 노드 위치를 정한 것

- 모든 원소는 서로 다른 유일한 키를 가진다.
- 왼쪽 서브 트리에 있는 원소들의 키는 그 루트의 키보다 작다
- 오른쪽 서브 트리에 있는 원소들의 키는 그 루트의 키보다 크다
- 왼쪽 서브 트리와 오른쪽 서브 트리도 이진 탐색 트리이다

** 이진탐색(탐색-O(logN), 삽입 삭제 불가능) + 연결 리스트(삽입 삭제 O(1) 탐색 O(n))

import os
import glob
import re
from bs4 import BeautifulSoup

# Unique Problem Bank for 19 Chapters
PROBLEM_BANK = {
    "1": {
        "mcq": {
            "title": "📝 깊이 있는 사유: 공진화의 이해",
            "desc": "기계와의 공진화(Symbiosis)에 대한 설명으로 가장 적절한 것은?",
            "options": [
                (False, "기계의 지능이 인간을 지배하도록 순응하는 과정입니다."),
                (True, "기계와 인간이 상호작용하며 서로의 발전을 견인하는 동반자적 관계입니다."),
                (False, "인간의 모든 인지적 노동을 기계에 완전히 위임하는 것입니다."),
                (False, "기계의 개입을 차단하고 아날로그 방식을 고집하는 것입니다."),
                (False, "AI가 스스로 독자적인 생태계를 구축하도록 방치하는 것입니다.")
            ],
            "success": "🎯 정답입니다! 공진화는 상호 보완적인 발전을 의미합니다.",
            "error": "❌ 아쉽습니다. 공진화는 일방적 지배나 위임이 아닙니다."
        },
        "dnd": {
            "title": "🧩 개념 복원 (Drag & Drop)",
            "desc": "인간과 AI의 관계를 나타내는 문장을 완성하세요.",
            "draggables": [("도구", "도구"), ("주체", "주체"), ("공진화", "공진화")],
            "text_html": '우리는 AI를 단순한 <span class="dropzone" data-target="도구"></span>(으)로만 보지 않고, 변화를 이끄는 <span class="dropzone" data-target="주체"></span>로서 함께 <span class="dropzone" data-target="공진화"></span>해야 합니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "현생 인류를 뜻하는 라틴어 학명으로, '지혜로운 인간'을 의미하는 단어는?",
            "target": "호모사피엔스,호모 사피엔스,사피엔스",
            "placeholder": "예: 호모 사피엔스"
        }
    },
    "2": {
        "mcq": {
            "title": "📝 깊이 있는 사유: 기술사적 맥락",
            "desc": "러다이트 운동이 현대 AI 시대에 주는 교훈으로 적절하지 않은 것은?",
            "options": [
                (False, "신기술에 대한 막연한 두려움은 근본적 해결책이 될 수 없습니다."),
                (False, "기술 도입으로 인한 노동 소외 현상에 주목해야 합니다."),
                (True, "기계를 물리적으로 파괴해야만 인간의 일자리를 지킬 수 있습니다."),
                (False, "기술 발전 과정에서 소외되는 계층을 위한 안전망이 필요합니다."),
                (False, "단순한 거부를 넘어 기술을 어떻게 통제할 것인가가 중요합니다.")
            ],
            "success": "🎯 정답입니다! 폭력적 거부보다는 지혜로운 수용과 통제가 필요합니다.",
            "error": "❌ 잘못된 접근입니다. 러다이트 운동의 한계를 떠올려보세요."
        },
        "dnd": {
            "title": "🧩 맥락 복원 (Drag & Drop)",
            "words": [("파괴", "파괴"), ("두려움", "두려움"), ("통제", "통제")],
            "text": '단순한 <span class="dropzone" data-target="두려움"></span>으로 인해 기계를 <span class="dropzone" data-target="파괴"></span>하기보다는, 인류의 가치에 맞게 <span class="dropzone" data-target="통제"></span>하는 법을 배워야 합니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "19세기 영국에서 일어난 기계 파괴 운동을 일컫는 용어는?",
            "target": "러다이트,Luddite",
            "placeholder": "예: 러다이트"
        }
    },
    "3": {
        "mcq": {
            "title": "📝 깊이 있는 사유: 질문의 힘",
            "desc": "AI 시대에 '비판적 질문'이 가지는 가치로 가장 올바른 것은?",
            "options": [
                (False, "AI의 처리 속도를 지연시키기 위한 목적입니다."),
                (False, "오로지 전문가들만이 가질 수 있는 특권입니다."),
                (False, "AI가 내놓은 모든 답을 무조건 부정하는 태도입니다."),
                (True, "환각 현상을 걸러내고 결과물의 진위를 판별하는 메타인지적 행위입니다."),
                (False, "기계가 스스로 질문하도록 학습시키는 코딩 기술입니다.")
            ],
            "success": "🎯 정확합니다! 주체적인 팩트 체크와 진위 판별이 핵심입니다.",
            "error": "❌ 아쉽습니다. 맹목적인 부정이나 기술적 지연이 아닙니다."
        },
        "dnd": {
            "title": "🧩 환각 현상 대처 (Drag & Drop)",
            "words": [("환각", "환각"), ("검증", "검증"), ("비판", "비판")],
            "text": 'AI가 사실인 것처럼 지어내는 <span class="dropzone" data-target="환각"></span> 현상에 맞서기 위해서는 끝없는 <span class="dropzone" data-target="검증"></span>과(와) <span class="dropzone" data-target="비판"></span>적 사고가 요구됩니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "AI가 거짓 정보를 마치 사실인 것처럼 그럴싸하게 생성해내는 오류를 무엇이라고 합니까?",
            "target": "환각,할루시네이션,Hallucination",
            "placeholder": "예: 환각"
        }
    },
    "4": {
        "mcq": {
            "title": "📝 깊이 있는 사유: 특이점과 통제",
            "desc": "초지능(AGI) 시대에 인류가 반드시 확보해야 할 역량은?",
            "options": [
                (False, "기계보다 더 빠르고 많은 양의 지식을 단순 암기하는 능력"),
                (True, "AI가 인류의 보편적 윤리와 공존하도록 가치를 정렬(Alignment)하는 역량"),
                (False, "모든 아날로그 시스템을 완벽한 디지털로 전환하는 기술력"),
                (False, "AI의 발전 속도를 늦추기 위한 물리적인 네트워크 차단 기술"),
                (False, "AI의 결정을 무비판적으로 수용하여 사회적 갈등을 없애는 태도")
            ],
            "success": "🎯 완벽합니다! 가치 정렬(Alignment)이 생존의 핵심입니다.",
            "error": "❌ 다시 생각해 보세요. 기계와의 연산 경쟁은 무의미합니다."
        },
        "dnd": {
            "title": "🧩 특이점 시대 대처 (Drag & Drop)",
            "words": [("정렬", "정렬"), ("윤리", "윤리"), ("방관", "방관")],
            "text": '우리는 AI의 발전을 <span class="dropzone" data-target="방관"></span>할 것이 아니라, 인류의 <span class="dropzone" data-target="윤리"></span>적 가치와 <span class="dropzone" data-target="정렬"></span>시켜야만 합니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "특정 분야에 국한되지 않고 인간이 할 수 있는 모든 지적 능력을 포괄적으로 갖춘 궁극의 인공지능을 가리키는 영문 약자는?",
            "target": "AGI,agi",
            "placeholder": "A로 시작하는 3글자 영문 약자"
        }
    },
    "5": {
        "mcq": {
            "title": "📝 깊이 있는 사유: 뇌 가소성",
            "desc": "AI 의존도가 높아지는 환경에서 우려되는 인간의 인지적 변화는?",
            "options": [
                (False, "뇌의 저장 용량이 물리적으로 증대된다."),
                (False, "멀티태스킹 능력이 끝없이 향상된다."),
                (True, "스스로 사고하고 기억하는 뇌 신경망의 퇴화(아웃소싱의 부작용)가 일어날 수 있다."),
                (False, "모든 인간의 지능 지수가 상향 평준화된다."),
                (False, "감정을 관장하는 뇌 영역이 발달하여 공감 능력이 저절로 커진다.")
            ],
            "success": "🎯 정답입니다! 의도적인 인지적 수고(마찰)를 유지해야 뇌 가소성을 긍정적으로 활용할 수 있습니다.",
            "error": "❌ 아쉽습니다. 뇌는 쓰지 않으면 퇴화합니다."
        },
        "dnd": {
            "title": "🧩 인지적 마찰 (Drag & Drop)",
            "words": [("가소성", "가소성"), ("마찰", "마찰"), ("위임", "위임")],
            "text": '사고 과정을 기계에 전면 <span class="dropzone" data-target="위임"></span>하면 뇌의 <span class="dropzone" data-target="가소성"></span>에 의해 뇌가소성이 저하되므로, 의도적인 인지적 <span class="dropzone" data-target="마찰"></span>이(가) 필요합니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "로크가 주장한 개념으로, 인간의 마음은 태어날 때 '백지 상태'와 같아 경험을 통해 쓰여진다는 라틴어는?",
            "target": "타불라라사,타불라 라사,Tabula Rasa",
            "placeholder": "예: 타불라 라사"
        }
    },
    "6": {
        "mcq": {
            "title": "📝 깊이 있는 사유: 교재의 해체",
            "desc": "생성형 AI 시대에 들어서며 교과서가 가지는 위상의 변화는?",
            "options": [
                (False, "절대적이고 유일무이한 지식의 원천으로 더욱 강화된다."),
                (False, "디지털로 포맷만 바뀐 채 내용은 영구히 불변하게 유지된다."),
                (True, "고정된 정전(Canon)의 위치에서 내려와, 다양한 정보원 중 하나의 레퍼런스로 변화한다."),
                (False, "학생들이 스스로 교과서를 폐기하고 AI 튜터만 바라보게 된다."),
                (False, "텍스트 중심에서 벗어나 오로지 영상 교재로만 대체된다.")
            ],
            "success": "🎯 정확합니다! 지식의 독점이 해체되고 교재는 유연한 참고 자료가 됩니다.",
            "error": "❌ 잘못된 이해입니다. 교과서의 절대성이 허물어집니다."
        },
        "dnd": {
            "title": "🧩 교과서의 의미 (Drag & Drop)",
            "words": [("정답", "정답"), ("해체", "해체"), ("질문", "질문")],
            "text": '고정된 지식의 <span class="dropzone" data-target="해체"></span>에 직면한 교실은 이제 하나의 <span class="dropzone" data-target="정답"></span>을 외우는 곳이 아니라, 무수한 <span class="dropzone" data-target="질문"></span>을 생산하는 공장이 되어야 합니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "역사의 발전을 설명하는 포괄적이고 거시적인 이데올로기나 철학적 틀. 포스트모더니즘과 AI에 의해 붕괴되고 있는 이것은?",
            "target": "거대서사,거대 서사",
            "placeholder": "예: 거대 서사"
        }
    },
    "7": {
        "mcq": {
            "title": "📝 깊이 있는 사유: 평가의 전환",
            "desc": "단편적 지식을 묻는 객관식 평가가 AI 시대에 효력을 상실한 가장 큰 이유는?",
            "options": [
                (False, "문제 출제에 드는 비용이 너무 많이 증가해서."),
                (True, "기계가 인간보다 압도적으로 빠르고 정확하게 정답을 도출해낼 수 있기 때문에."),
                (False, "학생들이 모두 정답을 맞혀 변별력이 사라졌기 때문에."),
                (False, "평가 시간이 너무 오래 걸려서."),
                (False, "온라인 시험 시스템이 불안정하기 때문에.")
            ],
            "success": "🎯 정답입니다. 기계가 압도하는 영역을 인간에게 평가하는 것은 무의미합니다.",
            "error": "❌ 아쉽습니다. 기계의 연산력 대체를 생각해보세요."
        },
        "dnd": {
            "title": "🧩 과정 중심 평가 (Drag & Drop)",
            "words": [("결과", "결과"), ("과정", "과정"), ("오류", "오류")],
            "text": '우리는 AI가 산출한 완벽한 <span class="dropzone" data-target="결과"></span>에 집착하지 말고, 학생이 겪은 혼란과 <span class="dropzone" data-target="오류"></span>를 분석하는 깊은 <span class="dropzone" data-target="과정"></span> 중심으로 평가를 옮겨야 합니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "주어진 정답을 찾는 대신, 문제를 해결하는 절차와 아이디어를 중시하는 평가 방식을 무엇 중심 평가라고 합니까?",
            "target": "과정,과정중심",
            "placeholder": "예: 과정 중심"
        }
    },
    "8": {
        "mcq": {
            "title": "📝 깊이 있는 사유: 영적 치유자로서의 교사",
            "desc": "AI 튜터가 보급된 이후 인간 교사의 핵심 역할로 올바른 것은?",
            "options": [
                (False, "수식과 영단어를 정확히 판서하고 암기를 점검하는 지식 전달자"),
                (False, "AI 시스템의 코드를 직접 수정하는 데이터 엔지니어"),
                (True, "학생의 정서적 결핍을 파악하고 동기를 부여하는 심리적 스캐폴더(Scaffolder)"),
                (False, "기계가 내린 평가를 학부모에게 단순히 전달하는 메신저"),
                (False, "모든 교실 통제권을 AI에게 넘기고 관망하는 구경꾼")
            ],
            "success": "🎯 완벽합니다! 온기를 나누고 용기를 주는 것이 교사의 본질입니다.",
            "error": "❌ 틀렸습니다. 기계가 대체할 수 없는 교사의 진정한 가치를 떠올리세요."
        },
        "dnd": {
            "title": "🧩 스캐폴딩의 본질 (Drag & Drop)",
            "words": [("지식", "지식"), ("스캐폴딩", "스캐폴딩"), ("온기", "온기")],
            "text": '단순한 <span class="dropzone" data-target="지식"></span> 주입을 넘어, 교사는 비고츠키의 <span class="dropzone" data-target="스캐폴딩"></span> 이론처럼 아이가 넘어지지 않도록 단단한 인간적 <span class="dropzone" data-target="온기"></span>(을)를 제공해야 합니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "러시아의 심리학자로, 학습자가 스스로 지식을 구성할 수 있도록 교사나 또래가 발판을 제공해야 한다는 이론을 주창한 학자는?",
            "target": "비고츠키,레프 비고츠키",
            "placeholder": "예: 비고츠키"
        }
    },
    "9": {
        "mcq": {
            "title": "📝 깊이 있는 사유: 디지털 판옵티콘",
            "desc": "교육 현장에 AI가 전면 도입될 때 발생할 수 있는 감시 체제의 부작용은?",
            "options": [
                (False, "교사들이 학생들의 성적을 알 수 없게 된다."),
                (True, "안면 인식 및 시선 추적 등으로 인해 학생의 모든 무의식마저 수치화되는 디지털 판옵티콘의 도래"),
                (False, "안전사고에 대비한 CCTV가 전부 무용지물이 된다."),
                (False, "학생들이 해킹 기술을 습득하여 관리 서버를 장악한다."),
                (False, "감시 센서의 전력 소비로 인해 교실의 온도가 상승한다.")
            ],
            "success": "🎯 정답입니다! 푸코가 경계한 자발적 복종과 규율의 감옥을 주의해야 합니다.",
            "error": "❌ 빙산의 일각입니다. 인간의 존엄성과 프라이버시 침해가 핵심입니다."
        },
        "dnd": {
            "title": "🧩 감시와 프라이버시 (Drag & Drop)",
            "words": [("자유", "자유"), ("감시", "감시"), ("수치화", "수치화")],
            "text": 'AI에 의한 완벽한 <span class="dropzone" data-target="수치화"></span>는 효율의 탈을 쓴 차가운 <span class="dropzone" data-target="감시"></span> 시스템이 되어 학생이 방황할 <span class="dropzone" data-target="자유"></span>마저 빼앗을 수 있습니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "영국의 벤담이 설계한 원형 감옥 구조. 감시자는 숨어있고 수감자는 항상 감시받는다고 느끼게 하는 이 구조의 이름은?",
            "target": "판옵티콘,파놉티콘,Panopticon",
            "placeholder": "예: 판옵티콘"
        }
    },
    "10": {
        "mcq": {
            "title": "📝 깊이 있는 사유: 에코체임버의 위험성",
            "desc": "알고리즘이 제공하는 초개인화 맞춤형 학습의 가장 큰 부작용은?",
            "options": [
                (False, "너무 많은 오프라인 토론이 강제되어 피로도가 쌓인다."),
                (False, "학생들의 학업 성취도가 하향 평준화된다."),
                (True, "자신과 비슷한 생각과 쉬운 정보만 반복 섭취하여 타인과의 연대(공통의 경험)를 상실하게 된다."),
                (False, "교과목의 갯수가 기하급수적으로 늘어난다."),
                (False, "시력 저하와 거북목 증후군이 발생한다.")
            ],
            "success": "🎯 정답입니다! 마이클 샌델이 지적하듯 파편화된 원자들의 고립을 막아야 합니다.",
            "error": "❌ 아쉽습니다. 인지적 고립과 사회성 붕괴에 초점을 맞추세요."
        },
        "dnd": {
            "title": "🧩 반향실 깨기 (Drag & Drop)",
            "words": [("편향", "편향"), ("에코체임버", "에코체임버"), ("충돌", "충돌")],
            "text": '알고리즘이 만든 <span class="dropzone" data-target="에코체임버"></span>에 갇혀 정보의 <span class="dropzone" data-target="편향"></span>성에 빠지지 않으려면, 이질적인 의견들과의 오프라인 <span class="dropzone" data-target="충돌"></span>이(가) 필수적입니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "비슷한 성향의 정보만 반복적으로 수용하여 닫힌 사고에 갇히는 현상을 뜻하는 5글자 단어는?",
            "target": "에코체임버,메아리방",
            "placeholder": "예: 에코체임버"
        }
    },
    "11": {
        "mcq": {
            "title": "📝 깊이 있는 사유: 잊혀질 권리",
            "desc": "학생들의 생체적/학습적 데이터가 영구적으로 클라우드에 박제될 때 발생하는 가장 치명적인 인권 침해는?",
            "options": [
                (False, "하드디스크 서버 유지비용이 폭증한다."),
                (True, "어린 시절의 실수와 치기 어린 편견들이 낙인효과를 일으켜 새롭게 변화할 기회(타불라 라사)를 원천 차단당하게 된다."),
                (False, "검색 속도가 느려진다."),
                (False, "광고성 이메일이 너무 많이 온다."),
                (False, "타인의 성적을 엿볼 수 있다.")
            ],
            "success": "🎯 정확합니다! 디지털 주홍글씨가 되어 아이들의 미래를 지배할 위험이 큽니다.",
            "error": "❌ 틀렸습니다. 데이터 주권과 존재론적인 낙인에 대한 윤리적 문제를 생각하세요."
        },
        "dnd": {
            "title": "🧩 디지털 권리 보호 (Drag & Drop)",
            "words": [("삭제", "삭제"), ("권리", "권리"), ("기억", "기억")],
            "text": '영구적으로 누적되는 클라우드의 폭력적인 <span class="dropzone" data-target="기억"></span>에 맞서, 아이들에게는 자신의 데이터를 <span class="dropzone" data-target="삭제"></span>할 수 있는 잊혀질 <span class="dropzone" data-target="권리"></span>가(이) 보장되어야 합니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "권력과 지식의 관계를 설파하며 기계적 통제와 규율을 예견했던 프랑스의 철학자는?",
            "target": "푸코,미셸 푸코,Foucault",
            "placeholder": "예: 푸코"
        }
    },
    "12": {
        "mcq": {
            "title": "📝 깊이 있는 사유: 의도적 마찰의 가치",
            "desc": "AI 튜터가 너무나 매끄럽고 완벽한 해답을 1초 만에 제공할 때, 교사가 취해야 할 올바른 전략은?",
            "options": [
                (False, "AI 모델의 유료 버전을 구독하여 답변 속도를 0.1초로 단축시킨다."),
                (False, "학생들이 정답을 그대로 필사하게 하여 진도를 빨리 뺀다."),
                (True, "답의 모순을 찾게 하거나 정답이 없는 토론을 유도하는 '의도적 마찰'을 설계한다."),
                (False, "AI 시스템의 전원을 아예 꺼버리고 평생 쓰지 않는다."),
                (False, "교사가 개입하지 않고 교실 밖으로 나간다.")
            ],
            "success": "🎯 정답입니다! 마찰(Friction)과 인지적 고통 없이는 진정한 통찰이 생겨나지 않습니다.",
            "error": "❌ 맹목적 효율성이나 완전한 배제는 답이 아닙니다. 비판적 과정을 유도해야 합니다."
        },
        "dnd": {
            "title": "🧩 비판적 수용 (Drag & Drop)",
            "words": [("매끄러움", "매끄러움"), ("마찰", "마찰"), ("성찰", "성찰")],
            "text": '기계가 제공하는 과도한 <span class="dropzone" data-target="매끄러움"></span>은(는) 인간의 사고를 좀먹습니다. 우리는 건강한 <span class="dropzone" data-target="마찰"></span>을 감내하며 치열한 자기 <span class="dropzone" data-target="성찰"></span>을 이루어야 합니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "주어진 정보를 수동적으로 받아들이는 것이 아니라, 전제와 근거의 타당성을 끊임없이 꼬집고 질문하는 사고방식은? (ㅇㅇ적 사고)",
            "target": "비판,비판적,비판적 사고,비판적사고",
            "placeholder": "예: 비판적 사고"
        }
    },
    "13": {
        "mcq": {
            "title": "📝 깊이 있는 사유: 프롬프트 리터러시",
            "desc": "'프롬프트 엔지니어링'을 교육할 때 단순히 명령어 입력 기술을 넘어 철학적으로 확장해야 하는 이유는?",
            "options": [
                (False, "코딩 문법이 매달 갱신되어 외우기 힘들기 때문이다."),
                (False, "AI를 이용하여 돈을 버는 방법을 가르치기 위해."),
                (True, "프롬프트는 단순히 기계를 부리는 스위치가 아니라, 세상을 바라보는 관점과 편견을 투영하는 질문의 그릇이기 때문이다."),
                (False, "학생들이 해킹을 배우지 못하도록 막기 위해."),
                (False, "외국어 학습을 더 효율적으로 하기 위해.")
            ],
            "success": "🎯 완벽합니다. 질문하는 방식이 곧 인간의 사유 능력을 결정합니다.",
            "error": "❌ 피상적인 코딩 기술이 아닙니다. 질문 안에 담긴 인문학적 깊이가 중요합니다."
        },
        "dnd": {
            "title": "🧩 질문의 격 (Drag & Drop)",
            "words": [("관점", "관점"), ("프롬프트", "프롬프트"), ("응답", "응답")],
            "text": '좋은 <span class="dropzone" data-target="프롬프트"></span>는 단어의 나열이 아니라 인간의 고유한 <span class="dropzone" data-target="관점"></span>을 담아야 하며, 그래야만 뻔하지 않은 훌륭한 <span class="dropzone" data-target="응답"></span>을 얻어낼 수 있습니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "문해력을 뜻하는 리터러시(Literacy)와 디지털(Digital)이 합성된 말로, 디지털과 AI 소양을 보편 교과로 삼아야 한다는 개념어는?",
            "target": "디지터시,Digitacy",
            "placeholder": "예: 디지터시"
        }
    },
    "14": {
        "mcq": {
            "title": "📝 깊이 있는 사유: 회복탄력성",
            "desc": "AI가 완벽한 맞춤형 학습으로 '실패 경험'을 제로로 만들어주는 환경이 아이의 정서에 미치는 불리한 영향은?",
            "options": [
                (False, "자신감이 우주를 뚫고 올라간다."),
                (False, "시험을 볼 때마다 시간이 단축된다."),
                (True, "단 한번이라도 AI의 도움을 받지 못하거나 현실의 거친 장벽을 마주했을 때 극단적으로 좌절하게 되는 '회복탄력성'의 상실."),
                (False, "신체 능력이 저하되어 운동을 기피하게 된다."),
                (False, "창의력이 기하급수적으로 폭발하게 된다.")
            ],
            "success": "🎯 정확한 통찰입니다! 실패의 백신을 맞지 않고 자란 아이는 작은 바이러스에 쓰러집니다.",
            "error": "❌ 역설을 이해해야 합니다. 완벽한 도우미는 온실 속 화초를 만듭니다."
        },
        "dnd": {
            "title": "🧩 정서의 힘 (Drag & Drop)",
            "words": [("실패", "실패"), ("연대", "연대"), ("회복탄력성", "회복탄력성")],
            "text": '아름다운 <span class="dropzone" data-target="실패"></span>의 기회를 학생들에게 허용해야 바닥에서 치고 올라오는 <span class="dropzone" data-target="회복탄력성"></span>이 길러지며, 이를 함께 견뎌내는 경험이 진정한 <span class="dropzone" data-target="연대"></span>를 만듭니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "타자의 얼굴을 마주하며 느끼는 무한한 윤리적 책임을 철학적으로 설파하여 교실 내 정서적 유대의 중요성을 일깨운 철학자의 이름은?",
            "target": "레비나스,에마뉘엘 레비나스",
            "placeholder": "예: 레비나스"
        }
    },
    "15": {
        "mcq": {
            "title": "📝 깊이 있는 사유: AI와 격차",
            "desc": "AI 시대의 교육 격차가 과거의 정보화 격차(Digital Divide)보다 훨씬 더 치명적이고 잔인한 이유는?",
            "options": [
                (False, "장비의 가격이 옛날 컴퓨터보다 수백 배 비싸기 때문이다."),
                (False, "와이파이가 끊기면 아무것도 할 수 없기 때문이다."),
                (True, "속도 차이를 넘어 인지적 확장성, 계급 재생산, 그리고 무의식의 지배라는 본질적 존재론의 격차를 낳기 때문이다."),
                (False, "선생님들이 AI를 다룰 준비가 전혀 안 되어있기 때문이다."),
                (False, "기계가 영어를 주로 사용해서 언어장벽이 크기 때문이다.")
            ],
            "success": "🎯 정답입니다. 기기에 대한 접근성을 넘어 통제권과 사유의 지배력을 가르는 계급 투쟁이 됩니다.",
            "error": "❌ 표면적 하드웨어의 문제를 넘어 철학적 권력의 문제입니다."
        },
        "dnd": {
            "title": "🧩 보편적 설계 (Drag & Drop)",
            "words": [("계급", "계급"), ("디바이드", "디바이드"), ("포용", "포용")],
            "text": '새로운 디지털 <span class="dropzone" data-target="디바이드"></span>가 단순한 자산의 척도를 넘어 새로운 <span class="dropzone" data-target="계급"></span>으로 굳건해지지 않도록, 교육 시스템은 절대적 <span class="dropzone" data-target="포용"></span>성을 입증해야 합니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "정의와 기회 평등의 문제를 치열하게 연구하며 '공정하다는 착각' 속 엘리트주의를 비판한 정치철학자는?",
            "target": "샌델,마이클 샌델,Sandel",
            "placeholder": "예: 마이클 샌델"
        }
    },
    "16": {
        "mcq": {
            "title": "📝 깊이 있는 사유: Opt-Out 조항",
            "desc": "학부모에게 '알고리즘 데이터 거부권(Opt-out)'을 보장해야 하는 근본적 윤리적 책무는 무엇인가?",
            "options": [
                (False, "서버 트래픽을 분산시키고 전기세를 절감하기 위한 조치이다."),
                (True, "나의 아이가 국가나 기업의 실험용 데이터 파이프로 전락하는 것을 인권의 차원에서 방어하기 위함이다."),
                (False, "오프라인 종이 교재 판매 수익을 보호하기 위함이다."),
                (False, "교육부의 업무 부담을 덜어주기 위해서이다."),
                (False, "아이들의 스마트폰 중독을 막기 위한 물리적 단절을 의미한다.")
            ],
            "success": "🎯 정확한 이해입니다. 거부할 권리는 디지털 인권의 시작점입니다.",
            "error": "❌ 틀렸습니다. 효용성보다 인권적 방어선의 문제입니다."
        },
        "dnd": {
            "title": "🧩 부모의 선택 (Drag & Drop)",
            "words": [("도구", "도구"), ("보호", "보호"), ("주권", "주권")],
            "text": '아이들을 알고리즘의 맹목적인 수집 <span class="dropzone" data-target="도구"></span>로 내몰지 않기 위해, 학부모는 데이터 <span class="dropzone" data-target="주권"></span>을 행사하여 적극적으로 자녀를 <span class="dropzone" data-target="보호"></span>해야 합니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "개인정보 수집 전 기본적으로 동의하지 않음을 전제로 하고, 서비스 제공을 거부할 권리를 부여하는 방식을 뜻하는 영어 약자는?",
            "target": "Opt-out,옵트아웃,Opt out",
            "placeholder": "예: Opt-out"
        }
    },
    "17": {
        "mcq": {
            "title": "📝 깊이 있는 사유: 혼돈의 공간",
            "desc": "AI 시대의 교실이 정돈된 '감옥(파놉티콘)'이 아닌 시끄러운 '아고라'가 되어야 하는 이유는?",
            "options": [
                (False, "학생들이 뛰어놀지 않으면 체력이 저하되기 때문이다."),
                (False, "기계를 작동시키는 환풍팬 소음이 커서 어차피 조용히 할 수 없기 때문이다."),
                (True, "규격화된 통제 속에서는 예측 불허의 갈등을 해결하는 거친 사회성과 시민 의식을 기를 수 없기 때문이다."),
                (False, "예산 부족으로 칸막이를 칠 수 없기 때문이다."),
                (False, "청소하기 편한 구조를 만들기 위해서이다.")
            ],
            "success": "🎯 정답입니다! 예측할 수 없는 갈등과 화해가 오가는 광장이 되어야 합니다.",
            "error": "❌ 아고라는 단순히 시끄러운 곳이 아니라 토론과 갈등 조정의 무대입니다."
        },
        "dnd": {
            "title": "🧩 공간의 재구성 (Drag & Drop)",
            "words": [("통제", "통제"), ("아고라", "아고라"), ("혼돈", "혼돈")],
            "text": '미래의 교실은 매끄러운 <span class="dropzone" data-target="통제"></span>의 공간을 부수고, 아이들이 서로 부딪히며 성장하는 민주주의적 <span class="dropzone" data-target="아고라"></span>의 건강한 <span class="dropzone" data-target="혼돈"></span>을 유지해야 합니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "고대 그리스의 광장으로, 토론하고 갈등하며 민주주의가 피어나던 곳을 비유하는 단어는?",
            "target": "아고라,Agora",
            "placeholder": "예: 아고라"
        }
    },
    "18": {
        "mcq": {
            "title": "📝 깊이 있는 사유: 글로벌 연대",
            "desc": "AI 기술의 범지구적 확산 속에서 K-에듀 모델이 세계에 기여할 수 있는 가장 철학적인 방향은?",
            "options": [
                (False, "한국어로 된 AI 모델을 세계 표준으로 강제 징수하는 것."),
                (False, "교육용 서버 클라우드 시장을 독점하여 막대한 외화를 벌어들이는 것."),
                (True, "가장 첨단화된 기저 위에 인간 교사의 사랑과 헌신이라는 아날로그 혼을 결합한 따뜻한 AI 생태계를 수출하는 것."),
                (False, "오직 성적과 입시 결과 최적화만을 목표로 하는 훈련 시스템을 파는 것."),
                (False, "개발도상국에 고전적인 칠판 교육 방식을 다시 판매하는 것.")
            ],
            "success": "🎯 정답입니다. 아시아적 헌신과 첨단 기술의 융합이 우리의 차별점입니다.",
            "error": "❌ K-에듀의 정수는 기계적 최적화가 아닌 교사의 유대와 책임 모델입니다."
        },
        "dnd": {
            "title": "🧩 인류애의 확산 (Drag & Drop)",
            "words": [("헌신", "헌신"), ("기술", "기술"), ("공존", "공존")],
            "text": '차가운 서구의 <span class="dropzone" data-target="기술"></span> 패권 중심주의를 넘어, 우리는 인간 중심의 아날로그적 <span class="dropzone" data-target="헌신"></span>을 입힌 평화로운 글로벌 <span class="dropzone" data-target="공존"></span> 생태계를 제안합니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "역경이나 실패에 좌절하지 않고 밑바닥에서 다시 튀어 오르는 심리적 근력을 의미하는 이 단어는 글로벌 연대에서도 중요하게 작용합니다.",
            "target": "회복탄력성,Resilience",
            "placeholder": "예: 회복탄력성"
        }
    },
    "19": {
        "mcq": {
            "title": "📝 깊이 있는 사유: 인간다움의 수호",
            "desc": "본서의 결론에서 강조하는, 기계가 도저히 모방할 수 없는 인류 최후의 프리미엄은 무엇인가?",
            "options": [
                (False, "거대한 분량의 텍스트를 기계보다 빠르게 읽어내는 속독 속해 능력"),
                (False, "복잡한 파이썬 코드를 에러 없이 암기하여 타이핑하는 기술"),
                (True, "타인의 슬픔을 읽어내고, 불완전함 속에서 상처입은 동료를 등 뒤에서 밀어주는 맹목적인 사랑"),
                (False, "어떤 상황에서도 절대 실패하지 않는 완결 무결한 논리력"),
                (False, "24시간 쉬지 않고 일할 수 있는 체력")
            ],
            "success": "🎯 가장 뜨거운 정답입니다! 불완전성의 사랑만이 우리의 가장 완벽한 무기입니다.",
            "error": "❌ 기계가 모방할 수 없는 아날로그적 온기와 연대를 놓치고 있습니다."
        },
        "dnd": {
            "title": "🧩 촛불의 의미 (Drag & Drop)",
            "words": [("불완전함", "불완전함"), ("알고리즘", "알고리즘"), ("사랑", "사랑")],
            "text": '기계의 완벽한 <span class="dropzone" data-target="알고리즘"></span>이 지배하려는 교실의 적막을 부수는 것은, 우리 인간의 <span class="dropzone" data-target="불완전함"></span>이 만들어내는 뜨겁고 투박한 <span class="dropzone" data-target="사랑"></span>뿐입니다.'
        },
        "sa": {
            "title": "⌨️ 핵심 어휘 회상",
            "desc": "기술 발전이 인간의 영혼과 존엄성을 해치지 않고, 기계와 인간이 상호 작용하며 함께 조화롭게 진화하는 것을 뜻하는 3글자 단어는?",
            "target": "공진화,공존",
            "placeholder": "예: 공진화"
        }
    }
}

def generate_widget_html(chapter_key, w_type):
    data = PROBLEM_BANK[chapter_key][w_type]
    if w_type == "mcq":
        html = f"""
<div class="interactive-widget mcq-widget" data-id="mcq-{chapter_key}">
    <h4 class="widget-title">{data['title']}</h4>
    <p style="margin-bottom:1.5rem;">{data['desc']}</p>
"""
        options_html = ""
        for is_correct, opt_text in data['options']:
            correct_str = "true" if is_correct else "false"
            options_html += f'    <div class="mcq-option" data-correct="{correct_str}">{opt_text}</div>\n'
        
        html += options_html
        html += f"""
    <button class="submit-btn" type="button">정답 제출하기</button>
    <div class="feedback-msg" data-success-msg="{data['success']}" data-error-msg="{data['error']}"></div>
</div>
"""
        return html
    elif w_type == "dnd":
        html = f"""
<div class="interactive-widget dnd-widget" data-id="dnd-{chapter_key}">
    <h4 class="widget-title">{data['title']}</h4>
    <p style="margin-bottom:1rem;">아래의 단어 블록을 드래그하여, 문맥상 알맞은 빈칸에 채워 넣으세요.</p>
    <div class="dnd-container">
"""
        for val, label in data['words'] if 'words' in data else data['draggables']:
            html += f'        <div class="draggable" data-value="{val}" draggable="true">{label}</div>\n'
        
        text_html = data['text'] if 'text' in data else data['text_html']
        html += f"""
    </div>
    <p style="font-size:1.15rem; line-height:2.0; margin-top:1.5rem; padding: 1.5rem; background: #fafafa; border:1px solid #e2e8f0; border-radius:8px; color: #334155;">
        {text_html}
    </p>
    <button class="submit-btn" type="button">정답 제출하기</button>
    <div class="feedback-msg"></div>
</div>
"""
        return html
    elif w_type == "sa":
        html = f"""
<div class="interactive-widget sa-widget" data-id="sa-{chapter_key}">
    <h4 class="widget-title">{data['title']}</h4>
    <p style="margin-bottom: 1rem;">{data['desc']}</p>
    <input class="short-answer-input" data-target="{data['target']}" placeholder="{data['placeholder']}" type="text"/>
    <button class="submit-btn" type="button">정답 제출하기</button>
    <div class="feedback-msg"></div>
</div>
"""
        return html

GLOSSARY_DB = {
    "판옵티콘": ("판옵티콘(Panopticon)", "영국의 철학자 제러미 벤담이 고안한 원형 감옥 구조. 감시자는 보이지 않으나 죄수는 항상 감시받는다고 느끼게 통제하는 시스템입니다.", "https://en.wikipedia.org/wiki/Panopticon"),
    "러다이트": ("러다이트(Luddite)", "19세기 영국에서 일어난 기계 파괴 운동. 신기술의 도입을 맹목적으로 거부하고 두려워하는 태도를 비유합니다.", "https://en.wikipedia.org/wiki/Luddite"),
    "타불라 라사": ("타불라 라사(Tabula Rasa)", "라틴어로 '백지 상태'를 의미하며, 인간의 마음은 비어 있고 경험에 의해 지식이 형성된다는 개념입니다.", "https://en.wikipedia.org/wiki/Tabula_rasa"),
    "호모 사피엔스": ("호모 사피엔스(Homo Sapiens)", "'지혜로운 인간'이라는 뜻으로, 현생 인류를 지칭합니다.", "https://en.wikipedia.org/wiki/Homo_sapiens"),
    "레비나스": ("에마뉘엘 레비나스(Emmanuel Levinas)", "타자의 얼굴과 윤리적 책임을 강조한 프랑스의 철학자입니다.", "https://en.wikipedia.org/wiki/Emmanuel_Levinas"),
    "푸코": ("미셸 푸코(Michel Foucault)", "권력과 지식의 관계, 감시 체계와 규율을 통찰한 프랑스의 사상가입니다.", "https://en.wikipedia.org/wiki/Michel_Foucault"),
    "비고츠키": ("레프 비고츠키(Lev Vygotsky)", "사회발달이론을 주창한 구소련의 심리학자로, 교사의 스캐폴딩(비계 설정)을 강조했습니다.", "https://en.wikipedia.org/wiki/Lev_Vygotsky"),
    "샌델": ("마이클 샌델(Michael Sandel)", "정의와 기회라는 주제를 깊이 연구한 정치철학자로, 공동체적 연대를 강조합니다.", "https://en.wikipedia.org/wiki/Michael_Sandel"),
    "벤담": ("제러미 벤담(Jeremy Bentham)", "영국의 공리주의 철학자이자 판옵티콘 구조의 창시자입니다.", "https://en.wikipedia.org/wiki/Jeremy_Bentham"),
    "거대 서사": ("거대 서사(Grand Narrative)", "역사의 발전을 설명하는 포괄적이고 거시적인 이데올로기나 철학적 틀을 의미합니다.", "https://en.wikipedia.org/wiki/Metanarrative"),
    "공진화": ("공진화(Symbiosis)", "서로 다른 개체가 상호작용하며 함께 진화하고 발전하는 현상을 뜻합니다.", "https://en.wikipedia.org/wiki/Symbiosis"),
    "회복탄력성": ("회복탄력성(Resilience)", "역경이나 실패에 좌절하지 않고 밑바닥에서 다시 튀어 오르는 심리적 근력을 의미합니다.", "https://en.wikipedia.org/wiki/Psychological_resilience"),
    "에코체임버": ("에코체임버(Echo Chamber)", "자신과 비슷한 성향의 정보만 반복적으로 수용하여 편향된 사고에 갇히는 현상을 의미합니다.", "https://en.wikipedia.org/wiki/Echo_chamber_(media)"),
    "환각": ("환각(Hallucination)", "인공지능이 사실이 아닌 내용을 마치 사실인 것처럼 그럴듯하게 생성해내는 오류 현상입니다.", "https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)")
}

def tone_patch(html_str):
    # Regex for tone patching `~다.` -> `~습니다.` excluding double quotes
    # Very crude but effective for plain body text ends.
    pattern = re.compile(r'([^"<>]{4,})(는다|이다|한다|웠다|했다|된다|있다)\.(?=[\s<]|$)')
    def repl(m):
        base = m.group(1)
        suffix = m.group(2)
        if suffix == '낸다': return base + '냅니다.'
        if suffix in ['는다', '한다', '된다']: return base + suffix[:-1] + '니다.'
        if suffix == '이다': return base + '입니다.'
        if suffix == '했다': return base + '했습니다.'
        if suffix == '웠다': return base + '웠습니다.'
        if suffix == '있다': return base + '있습니다.'
        return m.group(0)
    
    # We apply this multiple times because sentences might be grouped
    for _ in range(3):
        html_str = pattern.sub(repl, html_str)
    
    # Extra fix specifically for `~다.` which missed the above verb groups if it's simple verb
    html_str = re.sub(r'([^"<>]{4,})(으므로|기 때문이다)\.(?=[\s<]|$)', r'\1\2입니다.', html_str)

    return html_str

def fix_mermaid_syntax(html_str):
    # Missing quotes on node names with spaces: Root[AI 소양 ] -> Root["AI 소양"]
    # We will do a generic replacement for brackets
    def bracket_repl(m):
        inner = m.group(2).strip()
        if not inner.startswith('"') and not inner.startswith('<em>"'):
             inner = '"' + inner + '"'
        return m.group(1) + '[' + inner + ']'

    html_str = re.sub(r'([A-Za-z0-9_]+)\[(.*?)\]', bracket_repl, html_str)
    
    # Chapter 4 specific fix (missing closing quote)
    html_str = html_str.replace('B["인공일반지능 AGI - 범용적 인지 및 자율 판단]', 'B["인공일반지능 AGI - 범용적 인지 및 자율 판단"]')
    html_str = html_str.replace('B["인공일반지능 AGI - 범용적 인지 및 자율 판단] -->', 'B["인공일반지능 AGI - 범용적 인지 및 자율 판단"] -->')
    return html_str

def fix_mcq_script(html_str):
    # Modify the JS inside the html to read the custom success message from data attributes
    # The previous JS was hardcoded to `feedback.innerHTML = '🎯 <strong>정답입니다...';`
    js_target_success = "feedback.innerHTML = '🎯 <strong>정답입니다!</strong> 본문의 핵심 철학을 정확히 이해하셨습니다.';"
    js_target_error = "feedback.innerHTML = '❌ <strong>아쉽습니다.</strong> 기계적 효율성보다는 비판적 사고의 가치를 다시 떠올려보세요.';"
    
    new_success = "feedback.innerHTML = widget.querySelector('.feedback-msg').dataset.successMsg || '🎯 <strong>정답입니다!</strong>';"
    new_error = "feedback.innerHTML = widget.querySelector('.feedback-msg').dataset.errorMsg || '❌ <strong>아쉽습니다. 다시 시도해 보세요.</strong>';"
    
    html_str = html_str.replace(js_target_success, new_success)
    html_str = html_str.replace(js_target_error, new_error)
    return html_str

def process_file(filepath):
    # Extract chapter number
    filename = os.path.basename(filepath)
    match = re.search(r'chapter-(\d+)\.html', filename)
    if not match: return
    chap_num = match.group(1)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    article = soup.find(class_='article-content')
    if not article: return
    
    # 1. Clean old interactive widgets and old glossary to prevent dupes
    for cp in soup.find_all(class_='interactive-widget'): cp.decompose()
    for gl in soup.find_all(class_='glossary-section'): gl.decompose()
    
    # 2. Inject Unique Widgets
    h2_tags = article.find_all('h2')
    insert_points = [h for h in h2_tags if "성찰과 연대" not in h.get_text()]
    
    if chap_num in PROBLEM_BANK:
        types = ["mcq", "dnd", "sa"]
        w_idx = 0
        # Put one widget before the second h2, one before the third, and one before the reflection section
        # Spread them out
        intervals = len(insert_points) // 3
        if intervals == 0: intervals = 1
        
        for i, h2 in enumerate(insert_points):
            if i > 0 and i % intervals == 0 and w_idx < len(types):
                widget_soup = BeautifulSoup(generate_widget_html(chap_num, types[w_idx]), "html.parser")
                h2.insert_before(widget_soup)
                w_idx += 1
                
        # If any widgets left over, put them at the end before reflection
        reflection = article.find(class_='reflection-section')
        while w_idx < len(types):
            widget_soup = BeautifulSoup(generate_widget_html(chap_num, types[w_idx]), "html.parser")
            if reflection:
                reflection.insert_before(widget_soup)
            else:
                article.append(widget_soup)
            w_idx += 1

    # 3. Inject Deduplicated Glossary
    full_text = article.get_text()
    found_terms = []
    seen = set()
    for key, data in GLOSSARY_DB.items():
        if key in full_text and key not in seen:
            found_terms.append(data)
            seen.add(key)
            
    if found_terms:
        glossary_html = '<div class="glossary-section" style="margin-top: 4rem; padding: 2.5rem; background: #fafafa; border-radius:12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">'
        glossary_html += '<h3 style="margin-top:0; font-size:1.4rem; color:#0f172a; margin-bottom:1.5rem;">📖 용어 해설 (본문 인용)</h3><ul style="line-height:2.0; color:#334155; font-size:1.05rem;">'
        for data in found_terms:
            glossary_html += f'<li style="margin-bottom: 0.8rem;"><strong>{data[0]}</strong>: {data[1]} <a href="{data[2]}" target="_blank" style="color:#2563eb; text-decoration:none; font-size:0.9rem;">[위키백과 ↗]</a></li>'
        glossary_html += '</ul></div>'
        
        glossary_soup = BeautifulSoup(glossary_html, "html.parser")
        reflection = article.find(class_='reflection-section')
        if reflection:
            reflection.insert_before(glossary_soup)
        else:
            article.append(glossary_soup)

    # Output back to string
    out_html = str(soup)
    out_html = fix_mermaid_syntax(out_html)
    out_html = tone_patch(out_html)
    out_html = fix_mcq_script(out_html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(out_html)
    print(f"Processed Ch {chap_num} smoothly!")

if __name__ == "__main__":
    for filepath in glob.glob("d:/AIED2.0_docs/webbook/chapter-*.html"):
        if "chapter-20" not in filepath: # skip appendix
            process_file(filepath)

# acppred

By Daniela Peres Martinez

a tool to predict anticancer peptides 

## Setup

```
$ make setup
```
Objetivo geral da criação/utilização do código: O código criado foi utilizado para o desenvolvimento de uma página web para predição de peptideos com potencial atividade anticâncer.


Arquivo setup.py

O arquivo setup.py provavelmente é um dos arquivos mais significantes que deve ser adicionado no diretório de um projeto utilizando a linguagem Python. 
Seus maiores propósitos são:
Incluir opções e metadados sobre o programa, como o nome do pacote, versão, autor, arquivos de dados, entre outros.
Também serve com interface de linha de comando através do qual os comandos de empacotamento podem ser executados.

Palavras-chaves dentro do arquivo:

Packages: Lista de strings que especifica os pacotes que o setuptools irá manipular.

Entry_Points: Dicionário com chaves correspondentes aos nomes dos pontos de entrada e valores correspondentes aos pontos de entrada reais declarados no código fonte.

Setuptools: Setuptools é uma coleção de aprimoramentos para os distutils Python que permite que os desenvolvedores criem e distribuam os pacotes com mais facilidade, em especial aqueles que possuem dependências de outros pacotes. 

Distutils: Já o pacote distutils fornece um suporte para a construção e instalação de módulos adicionais em uma instalação do Python.


Arquivo requirements.txt
Esse arquivo contém uma lista com itens/pacotes que serão instalados, neste caso:

Scikit-learn: biblioteca de código aberto, que fornece vários recursos para modelagem estatística e suporte para aprendizagem de máquina supervisionado ou não supervisionado. Oferece variedade de algoritmos integrados, como algoritmos de classificação, regressão, agrupamento, redução de dimensionalidade, entre outros.

Umap-learn: UMAP é a sigla para Uniform Manifold Approximation and Projection, um algoritmo utilizado para a redução dimensional. Sua implementação está disponível através da utilização do pacote python Umap-learn. 

Imbalanced-learn: é uma biblioteca licenciada pelo MIT de código aberto que depende também da utilização do scikit-learn, e é utilizada pois fornece ferramentas para o trabalhado com classificação de classes desequilibradas.

Ploty: é uma biblioteca de código aberto que oferece suporte para mais de 40 tipos de gráficos exclusivos, para usos estatísticos, financeiros, científicos, entre outros, a biblioteca permite que os desenvolvedores criem visualizações interativas baseadas na web que podem ser visualizadas tanto em notebooks jupyter, quanto em arquivos HTML ou parte de aplicativos web desenvolvidos unicamente com Python.

Pandas: outro pacote de código aberto que bastante utilizado para análise de dados e aprendizado de máquina, o pandas é construídos sobre um outro código denominado Numpy, este oferece suporte para arrays multidimensionais.

Numpy: o numpy é capaz de suportar o processamento de arranjos e matrizes multi-dimensionais e apresenta uma grande coleção de funções matemáticas para operar sobre estas matrizes.

Biopython: é uma biblioteca para manipulação de dados biológicos.

Pytest: o pytest é uma framework utilizada para criação de testes de uma maneira mais rápida e dinâmica.

Flask: o flask é utilizado para desenvolver aplicações web que utilizam python, é classificado como um miniframework pois não necessita de ferramentas ou bibliotecas particulares.

Gunicorn: é um servidor python WSGI HTTP, amplamente compatível com diferentes frameworks da web, pode ser implementado de forma simples, é leve nos recursos do servidor e bastante rápido.


Arquivo environment.yml
Um arquivo environment.yml nos mostra a lista de dependências, e em quais canais prioriza-se que estas sejam baixadas, neste caso:

	Canais:
Bioconda: O canal bioconda possibilita a instalação de pacotes que estão relacionados com pesquisas dos campos biomédicos.
Conda-forge: é um organização comunitária do GitHub, que contém diferentes receitas conda, ou seja, fornece pacotes conda para diferentes softwares.

	Dependências: dependências do software são as bibliotecas ou pacotes que são reutilizados um novo software.
  
  
Arquivo Makefile
Os arquivos makefile são criados para que se possa executar ou atualizar uma tarefa quando determinados arquivos forem atualizados. O arquivo makefile determina qual o conjunto de tarefas que deve ser executado. De maneira geral, o makefile também pode ser utilizado para automatização do processo de construção de um software e tarefas complexas com dependências. 

conda env create: criação de um ambiente para desenvolvimento Python utilizando o conda. 
conda env update: atualização para a última versão.


Arquivo .gitignore

O arquivo .gitignore informa ao Git quais são os arquivos que devem ser ignorados no momento em que o projeto é enviado para o repositório GitHub.


PASTA TESTS:

Arquivo test_model.py

Palavras-chaves dentro do arquivo:

RandomForestClassifier: Meta estimador que ajusta vários classificadores de árvores de decisão em várias subamostras do conjunto de dados, e usa então a média para melhorar a precisão preditiva e controlar o ajuste excessivo.

import os: as funções pertencentes ao módulo os permitem operar tarefas subjacentes do sistema operacional, independente de qual este seja.

def: definir função.

test_model_train( ): o treinamento do modelo mede a precisão.

estimator: o estimator é um objeto que se ajusta a um modelo com base em alguns dados de treinamento e é então capaz de inferir algumas propriedades em novos dados, exemplos podem ser classificadores ou regressores.

assert: continua-se a execução se a condição avaliada for considerada verdadeira, se for considerada falsa - AssertionError.

isinstance: esta função retorna como verdadeira se o objeto for do tipo especificado, se não for, retorna como falsa.

str: o método str converte os dados em strings. 

transform ( ): permite que você execute uma função para cada valor do DataFrame.

save( ): salva uma matriz em um arquivo binário em NumPy formato npy.

Pickle: é usado para serialização e deserialização da estrutura de um objeto python, ou seja, converte um objeto python em um fluxos de bytes para armazená-lo em um banco de dados, por exemplo.


PASTA NOTEBOOKS
	Criada no Jupyter Notebooks

Arquivo EDA.ipynb
	
A análise exploratória de dados (EDA) é uma abordagem para análise de conjuntos de dados que resume as principais características destes, podendo ou não um método estatístico ser utilizado.
	
Temos uma lista de peptídeos que conhecidamente apresentam atividade anticâncer e uma lista de peptídeos que até o momento não se conhece atividade anticâncer nestes. A lista foi retirada do banco de dados AntiCP 2.0. Podemos observar na tabela (Out20) a quantidade de aminoácidos que constitui cada um dos peptídeos analisados.

Palavras-chave:
	
Label: classe para exibição de texto ou imagem.

Sillhouette_score: coeficiente calculado utilizando a distância média intra-cluster e distância média do cluster mais próximo para cada amostra.

train_test_split: utilizado para divir arrays ou matrizes em subconjuntos aleatórios para treino e para teste.

classification_report: ocorre a construção de um relatório texto que mostra as principais métricas de classificação que foram geradas.

return: utilizado para finalização da chamada de função e “retorna” o resultado.

Com a análise exploratória de dados também podemos observar os parâmetros que foram gerados em relação aos valores de precisão do modelo (grau de variação dos resultados que foram medidos), assim como os resultados de recall (parâmetros sobre a sensibilidado do modelo que foi criado), além disso temos detalhes do f-1 score, que também faz parte das medidas de precisão do modelo, justamente utilizando-se dos resultados da precisão e dos valores de recall.


PASTA DATA

Arquivo results.cvs
Mostra os resultados de predição que foram gerados, com os nomes que foram colocados nos peptídeos analisados.
Arquivo models.pickle
Meu github mostrava a seguinte mensagem ao abrir este arquivo: “(Sorry about that, but we can’t show files that are this big right now.)”
Arquivo example.fasta
Arquivo com os nomes atribuídos as sequências fastas utilizadas dos peptídeos que foram analisados, mas ainda sem o valor atribuído após a análise.


PASTA TESTS:
	
Arquivo model.pickle: não aparecia nada neste arquivo, apesar de marcar 782 bytes.


PASTA RAW:

Contém um arquivo negative.txt e um positive.txt que são as listas de peptídeos que não apresentam atividade anticâncer conhecida e a lista que possui atividade anticâncer conhecida.


PASTA MODELS:

Contém um arquivo model.pickle que ao abrir aparecia a mensagem (Sorry about that, but we can’t show files that are this big right now.) (1.78 MB).


PASTA ACPPRED

templates/index.html
Pasta templates com o único arquivo index.html, ou seja, um arquivo que contém o texto que será visualizado na página de predição de epítopos anticâncer quando esta for acessada.

<!DOCTYPE html>: tag utilizada para especificar qual é a versão do HTML o documento está utilizando, chamado de declaração do tipo de documento.

<html lang="en">: atributo que ajuda a definir o idioma de um elemento, ou seja, a língua em que elementos não editáveis serão escritos, ou a língua em que elementos editáveis deverão ser escritos pelo usuário.

<head>: “cabeça” do documento HTML, serve para as informações gerais (metadados) do documento, como títulos, links para scripts e outros, dentro dessa temos a indicação com o comando de codificação dos caracteres que serão utilizados (<meta charset="UTF-8">) e também a indicação do título da página (acppred) e indicação do término da cabeça do documento <head> e o início do “corpo do texto”.

<body>: representa o contéudo em sí do documento em HTML.

<hr>: representa uma mudança entre elementos em nível de parágrafos, por exemplo.

</div>: é um container para agrupar elementos.

</form>: submete os dados que o usuário der entrada para um programa que se encarregará de processar esses dados, de acordo com aquilo que o desenvolvedor solicitou do programa.	


Arquivo models.py

Modelos são geralmente definidos no arquivo models.py em uma aplicação.
	
Palavras-chave:

Bio.SeqUtils import ProtParam: é utilizado para análise de proteínas.

sklearn.ensemble: os métodos ensemble combinam as previsões de vários estimadores de base que foram construídos com um determinado algoritmo de aprendizado para que se possa melhorar a robustez de um único estimador.

__init__: a função __init__ deve ser chamada toda vez que deseja-se criar um objeto a partir de uma classe, com o __init__ a classe inicia os atributos do objeto e não serve para outros propósitos, sendo usado somente dentro das classes.

args: com o args permite-se que um número não especificado de argumentos seja passado para uma função (args, de arguments).

open: a função open abre um arquivo e retorna este como um objeto de arquivo.

append: utilizado para adicionar itens ao final de uma lista.

fit: utilizado para o ajuste do modelo aos dados de treinamento.

predict: permite a previsão dos rótulos dos valores de dados com base no modelo treinado.

predict_proba: é um método em classificadores e clusterers capaz de retornar estimativas de probabilidade para cada classe.

write: usado para escrever em um arquivo utilizando o objeto do arquivo, o método write( ) grava strings no arquivo.

dumps: o método dumps é utilizado quando os objetos python precisam ser armazenados em um arquivo e também quando os objetos precisam estar no formado de strings.

@statiticmethod: quando este método é chamado é possível colocar uma função dentro de uma classe, mas não é possível acessar a instância dessa classe.

loads: é usado para converter o documento JSON string no dicionário python de arquivos utilizado para ler arquivos de texto, arquivos binário ou arquivos JSON.

read( ): retorna o número especificado de bytes de um arquivo.


Arquivo predict.py

Palavras-chave:

argparse: módulo que facilita a criação de interfaces de linha de comando amigáveis.

SeqIO: fornece uma interface simples para entrada e saída de vários formatos de arquivo de sequência e existe a interface irmã Bio.

main: significa o ambiente principal onde o código é executado.

add_argument: anexa especificações de argumentos individuais ao analisador.

parse_args( ): executa o analisador e coloca os dados extraídos em um objeto argparse.


Arquivo serve.py

Palavras-chave:
	
@app.route: o roteamento de aplicativo significa mapear a URL para uma função específica que irá manipular a lógica dessa URL.

index( ): ajuda a encontrar a posição de índice de um elemento, ou ítem em uma string de caracteres.

render_template: para a renderização do template.

method =: uma função que pertence a um objeto.

get: o método get retorna com o valor do item com a chave que foi especificada. 


Arquivo train.py

Palavras-chave: 
	
print: exibe as mensagens na tela.


Arquivo utils.py
	
Lista das letras que são permitidas como válidas para compor a listagem de peptídeos.









